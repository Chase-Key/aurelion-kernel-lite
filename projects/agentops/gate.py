"""
gate.py — Demo password gate for AgentOps Console.

Set DEMO_PASSWORD via Fly secrets to restrict access to invited guests only.
If DEMO_PASSWORD is not set the gate is open (local dev default).
"""
from __future__ import annotations

import hashlib
import os
from urllib.parse import parse_qs

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse

_PASSWORD: str = os.getenv("DEMO_PASSWORD", "")
_COOKIE: str = "demo_auth"

# Paths that never require authentication
# /ingest/trace is auth-exempt here; the endpoint enforces its own API key check.
_PUBLIC: frozenset = frozenset({"/login", "/logout", "/health", "/ingest/trace"})

_LOGIN_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>AgentOps Console — Access Required</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #0a0d12;
      color: #e2e8f0;
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .gate {
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 16px;
      padding: 3rem 2.5rem;
      width: 100%;
      max-width: 400px;
      text-align: center;
    }
    .icon { font-size: 2.5rem; margin-bottom: 1.25rem; }
    h1 { font-size: 1.25rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.4rem; }
    .badge {
      display: inline-block;
      background: rgba(0,212,255,0.12);
      color: #00d4ff;
      font-size: 0.7rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 1.5rem;
    }
    .sub { font-size: 0.85rem; color: #6b7280; margin-bottom: 2rem; line-height: 1.5; }
    input[type=password] {
      width: 100%;
      background: #1a2233;
      border: 1px solid #374151;
      border-radius: 8px;
      color: #e2e8f0;
      padding: 0.8rem 1rem;
      font-size: 0.95rem;
      outline: none;
      margin-bottom: 0.75rem;
      transition: border-color 0.15s;
    }
    input[type=password]:focus { border-color: #00d4ff; }
    button {
      width: 100%;
      background: #00d4ff;
      color: #0a0d12;
      border: none;
      border-radius: 8px;
      padding: 0.8rem;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      letter-spacing: 0.02em;
      transition: background 0.15s;
    }
    button:hover { background: #00b8d9; }
    .error { color: #f87171; font-size: 0.82rem; margin-bottom: 0.75rem; }
    .footer { margin-top: 1.75rem; font-size: 0.78rem; color: #4b5563; }
    .footer a { color: #6b7280; text-decoration: none; }
    .footer a:hover { color: #00d4ff; }
  </style>
</head>
<body>
  <div class="gate">
    <div class="icon">🤖</div>
    <h1>AgentOps Console</h1>
    <div class="badge">INVITE ONLY</div>
    <p class="sub">Multi-model AI agent testing platform.<br>This demo is by invitation.</p>
    <!-- ERROR_PLACEHOLDER -->
    <form method="post" action="/login">
      <input type="password" name="password" placeholder="Enter demo password" autofocus autocomplete="current-password">
      <button type="submit">Enter Console</button>
    </form>
    <div class="footer">
      Don't have access?
      <a href="https://app.reclaim.ai/m/chase-key/meet-with-chase" target="_blank" rel="noopener">
        Request a demo →
      </a>
    </div>
  </div>
</body>
</html>"""


def _cookie_val() -> str:
    return hashlib.sha256(_PASSWORD.encode()).hexdigest()


def _is_auth(request: Request) -> bool:
    if not _PASSWORD:
        return True
    return request.cookies.get(_COOKIE) == _cookie_val()


def login_page(error: str = "") -> HTMLResponse:
    html = _LOGIN_HTML.replace(
        "<!-- ERROR_PLACEHOLDER -->",
        f'<p class="error">{error}</p>' if error else "",
    )
    return HTMLResponse(html, status_code=401 if error else 200)


async def handle_login(request: Request) -> RedirectResponse | HTMLResponse:
    """Verify submitted password and set auth cookie, or return error page."""
    body = await request.body()
    data = parse_qs(body.decode())
    submitted = data.get("password", [""])[0]
    if _PASSWORD and submitted == _PASSWORD:
        resp = RedirectResponse("/", status_code=302)
        resp.set_cookie(_COOKIE, _cookie_val(), httponly=True, samesite="lax", max_age=86400 * 7)
        return resp
    return login_page("Incorrect password. Request access below.")


class DemoGate(BaseHTTPMiddleware):
    """Middleware that enforces the demo password gate on all non-public routes."""

    async def dispatch(self, request: Request, call_next):
        if request.url.path in _PUBLIC or request.url.path.startswith("/static"):
            return await call_next(request)
        if _is_auth(request):
            return await call_next(request)
        return RedirectResponse("/login", status_code=302)
