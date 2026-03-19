"""
aurelion_agent.server — AgentServer: wrap any BaseAgent as a streaming web UI.

Provides a minimal, self-contained chat interface served from a single Python
process. No frontend build step, no external CDN, no separate server config.

Endpoints:
    GET  /                    → Chat UI (browser)
    GET  /health              → {"status": "ok", "agent": name}
    POST /chat                → {"message": "..."} → {"response": "...", "latency_ms": float}
    GET  /chat/stream?message= → SSE token stream (used by the UI)

Usage:
    from aurelion_agent import AgentServer

    class MyAgent(BaseAgent):
        def build_system_prompt(self):
            return "You are a helpful assistant."

    agent = MyAgent("Demo", llm=LLMProvider())
    server = AgentServer(agent)
    server.run()  # → http://localhost:8080

Or use the underlying FastAPI app directly:
    import uvicorn
    uvicorn.run(server.app, host="0.0.0.0", port=8080)
"""

from __future__ import annotations

import json
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base_agent import BaseAgent


# ---------------------------------------------------------------------------
# Embedded UI — single self-contained HTML/CSS/JS, no CDN, no build step
# ---------------------------------------------------------------------------

def _build_ui(agent_name: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AURELION — {agent_name}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background: #0d0d0d;
      color: #e2e2e2;
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      font-size: 15px;
      height: 100dvh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    /* ── Header ── */
    header {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid #1e1e1e;
      background: #0d0d0d;
      flex-shrink: 0;
    }}
    .brand {{
      font-size: 0.6rem;
      font-weight: 700;
      letter-spacing: 0.18em;
      color: #444;
      text-transform: uppercase;
    }}
    .sep {{ color: #333; }}
    .agent-name {{
      font-size: 0.9rem;
      font-weight: 600;
      color: #ccc;
    }}
    #dot {{
      width: 7px; height: 7px;
      border-radius: 50%;
      background: #22c55e;
      margin-left: auto;
      transition: background 0.3s;
    }}
    #dot.busy {{ background: #f59e0b; }}
    #dot.error {{ background: #ef4444; }}

    /* ── Messages ── */
    #feed {{
      flex: 1;
      overflow-y: auto;
      padding: 1.25rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      scroll-behavior: smooth;
    }}
    #feed::-webkit-scrollbar {{ width: 4px; }}
    #feed::-webkit-scrollbar-track {{ background: transparent; }}
    #feed::-webkit-scrollbar-thumb {{ background: #2a2a2a; border-radius: 2px; }}

    .msg {{
      max-width: min(72%, 640px);
      padding: 0.65rem 0.9rem;
      border-radius: 14px;
      line-height: 1.6;
      font-size: 0.88rem;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    .msg.user {{
      align-self: flex-end;
      background: #1b3a5c;
      color: #ddeeff;
      border-radius: 14px 14px 3px 14px;
    }}
    .msg.agent {{
      align-self: flex-start;
      background: #181818;
      border: 1px solid #242424;
      border-radius: 3px 14px 14px 14px;
      color: #e2e2e2;
    }}
    .msg.agent.typing {{
      border-color: #2e2e2e;
    }}
    .msg.system {{
      align-self: center;
      font-size: 0.78rem;
      color: #555;
      background: transparent;
      border: none;
      padding: 0.2rem 0;
    }}

    /* blinking cursor during streaming */
    .cursor {{
      display: inline-block;
      width: 2px; height: 0.9em;
      background: #666;
      margin-left: 1px;
      vertical-align: text-bottom;
      animation: blink 0.9s step-end infinite;
    }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}

    /* ── Input bar ── */
    footer {{
      flex-shrink: 0;
      display: flex;
      align-items: flex-end;
      gap: 0.6rem;
      padding: 0.85rem 1rem;
      border-top: 1px solid #1e1e1e;
      background: #0d0d0d;
    }}
    #input {{
      flex: 1;
      background: #181818;
      border: 1px solid #2a2a2a;
      border-radius: 10px;
      padding: 0.6rem 0.85rem;
      color: #e2e2e2;
      font-size: 0.88rem;
      font-family: inherit;
      line-height: 1.5;
      resize: none;
      outline: none;
      max-height: 7rem;
      overflow-y: auto;
      transition: border-color 0.15s;
    }}
    #input::placeholder {{ color: #3a3a3a; }}
    #input:focus {{ border-color: #3a3a3a; }}

    #send {{
      background: #1b3a5c;
      color: #ddeeff;
      border: none;
      border-radius: 10px;
      padding: 0.6rem 1.1rem;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 500;
      font-family: inherit;
      white-space: nowrap;
      transition: background 0.15s, opacity 0.15s;
      line-height: 1.5;
    }}
    #send:hover:not(:disabled) {{ background: #254f7a; }}
    #send:disabled {{ opacity: 0.35; cursor: not-allowed; }}

    /* ── Responsive ── */
    @media (max-width: 600px) {{
      .msg {{ max-width: 90%; }}
    }}
  </style>
</head>
<body>
  <header>
    <span class="brand">AURELION</span>
    <span class="sep">·</span>
    <span class="agent-name">{agent_name}</span>
    <span id="dot"></span>
  </header>

  <div id="feed"></div>

  <footer>
    <textarea id="input" rows="1" placeholder="Send a message... (Enter to send, Shift+Enter for newline)"></textarea>
    <button id="send">Send</button>
  </footer>

  <script>
    const feed   = document.getElementById('feed');
    const input  = document.getElementById('input');
    const send   = document.getElementById('send');
    const dot    = document.getElementById('dot');
    let   busy   = false;

    function setDot(state) {{
      dot.className = state === 'idle' ? '' : state;
    }}

    function addMsg(role, text) {{
      const el = document.createElement('div');
      el.className = 'msg ' + role;
      el.textContent = text;
      feed.appendChild(el);
      feed.scrollTop = feed.scrollHeight;
      return el;
    }}

    function autosize() {{
      input.style.height = 'auto';
      input.style.height = Math.min(input.scrollHeight, 112) + 'px';
    }}

    async function submit() {{
      const text = input.value.trim();
      if (!text || busy) return;
      busy = true;
      send.disabled = true;
      setDot('busy');

      input.value = '';
      input.style.height = 'auto';

      addMsg('user', text);

      const agentEl = addMsg('agent', '');
      agentEl.classList.add('typing');
      const cursor = document.createElement('span');
      cursor.className = 'cursor';
      agentEl.appendChild(cursor);

      const url = '/chat/stream?message=' + encodeURIComponent(text);
      const evs = new EventSource(url);

      evs.onmessage = (e) => {{
        const data = JSON.parse(e.data);
        if (data.done) {{
          evs.close();
          agentEl.classList.remove('typing');
          cursor.remove();
          setDot('idle');
          send.disabled = false;
          busy = false;
          input.focus();
          return;
        }}
        if (data.token) {{
          agentEl.insertBefore(document.createTextNode(data.token), cursor);
          feed.scrollTop = feed.scrollHeight;
        }}
        if (data.error) {{
          agentEl.classList.remove('typing');
          cursor.remove();
          agentEl.textContent = '⚠ ' + data.error;
          agentEl.style.color = '#ef4444';
          evs.close();
          setDot('error');
          send.disabled = false;
          busy = false;
        }}
      }};

      evs.onerror = () => {{
        evs.close();
        agentEl.classList.remove('typing');
        cursor.remove();
        if (!agentEl.textContent) {{
          agentEl.textContent = '⚠ Could not reach the agent. Is the server running?';
          agentEl.style.color = '#ef4444';
        }}
        setDot('error');
        send.disabled = false;
        busy = false;
      }};
    }}

    send.addEventListener('click', submit);
    input.addEventListener('input', autosize);
    input.addEventListener('keydown', (e) => {{
      if (e.key === 'Enter' && !e.shiftKey) {{
        e.preventDefault();
        submit();
      }}
    }});

    // Focus on load
    input.focus();
  </script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# AgentServer
# ---------------------------------------------------------------------------

class AgentServer:
    """
    Wrap any BaseAgent as a streaming HTTP server with a built-in chat UI.

    Requires: fastapi, uvicorn  (pip install aurelion-agent[server])

    Args:
        agent: Any BaseAgent subclass instance.
        host: Bind address. Default "127.0.0.1" (localhost only).
              Use "0.0.0.0" to expose on your network or for Fly.io.
        port: Port to listen on. Default 8080.
        title: Optional display name override for the UI header.
               Defaults to agent.name.
        allow_origins: List of allowed CORS origins (for external frontends).
                       Default ["*"] when host is "0.0.0.0", else None.
    """

    def __init__(
        self,
        agent: "BaseAgent",
        host: str = "127.0.0.1",
        port: int = 8080,
        title: str | None = None,
        allow_origins: list[str] | None = None,
    ):
        self._agent = agent
        self._host = host
        self._port = port
        self._title = title or agent.name
        self._allow_origins = allow_origins

        self._app = self._build_app()

    @property
    def app(self):
        """The underlying FastAPI application. Use for custom mounting or testing."""
        return self._app

    def _build_app(self):
        try:
            from fastapi import FastAPI, Request
            from fastapi.middleware.cors import CORSMiddleware
            from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
        except ImportError as exc:
            raise ImportError(
                "fastapi is required for AgentServer. "
                "Install it with: pip install 'aurelion-agent[server]'"
            ) from exc

        app = FastAPI(title=f"AURELION — {self._title}", docs_url=None, redoc_url=None)

        if self._allow_origins:
            app.add_middleware(
                CORSMiddleware,
                allow_origins=self._allow_origins,
                allow_methods=["GET", "POST"],
                allow_headers=["*"],
            )

        ui_html = _build_ui(self._title)

        @app.get("/", response_class=HTMLResponse, include_in_schema=False)
        def index():
            return HTMLResponse(content=ui_html)

        @app.get("/health")
        def health():
            return {"status": "ok", "agent": self._agent.name}

        @app.post("/chat")
        def chat(body: dict):
            message = (body.get("message") or "").strip()
            if not message:
                return JSONResponse({"error": "message is required"}, status_code=400)
            t0 = time.monotonic()
            trace = self._agent.respond(message)
            latency_ms = round((time.monotonic() - t0) * 1000, 1)
            return {"response": trace.last_response, "latency_ms": latency_ms}

        @app.get("/chat/stream")
        def stream(message: str = ""):
            message = message.strip()
            if not message:
                return JSONResponse({"error": "message is required"}, status_code=400)

            def sse():
                try:
                    for chunk in self._agent.stream_respond(message):
                        yield f"data: {json.dumps({'token': chunk})}\n\n"
                except Exception as exc:
                    yield f"data: {json.dumps({'error': str(exc)})}\n\n"
                finally:
                    yield f"data: {json.dumps({'done': True})}\n\n"

            return StreamingResponse(
                sse(),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "X-Accel-Buffering": "no",  # disables Nginx buffering for SSE
                },
            )

        return app

    def run(self, reload: bool = False) -> None:
        """
        Start the server. Blocks until interrupted (Ctrl+C).

        Args:
            reload: Enable auto-reload on file changes (dev mode only).
        """
        try:
            import uvicorn
        except ImportError as exc:
            raise ImportError(
                "uvicorn is required to run AgentServer. "
                "Install it with: pip install 'aurelion-agent[server]'"
            ) from exc

        print(f"\n  AURELION AgentServer")
        print(f"  Agent : {self._agent.name}")
        print(f"  UI    : http://{self._host}:{self._port}")
        print(f"  Press Ctrl+C to stop\n")

        uvicorn.run(
            self._app,
            host=self._host,
            port=self._port,
            log_level="warning",
            reload=reload,
        )
