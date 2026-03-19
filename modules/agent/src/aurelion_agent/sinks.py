"""
aurelion_agent.sinks — Pre-built trace sinks for BaseAgent.

A trace sink is any callable with signature:
    (trace: AgentTrace) -> None

Configure on any agent at construction time:

    from aurelion_agent import BaseAgent, LLMProvider
    from aurelion_agent.sinks import FileSink, AgentOpsSink, stdout_sink

    agent = MyAgent(
        name="demo",
        llm=LLMProvider(),
        trace_sinks=[
            stdout_sink,
            FileSink("traces/my_agent.jsonl"),
            AgentOpsSink("http://localhost:8090"),
        ],
    )

Every respond() and stream_respond() call automatically fires all sinks.
Sink failures are silenced — a broken sink never crashes your agent.

Built-in sinks
--------------
stdout_sink         Print a one-line summary to stderr (dev/debugging)
FileSink(path)      Append full traces as JSONL lines to a local file
AgentOpsSink(url)   POST traces to a self-hosted AgentOps Console

This is what LangSmith charges $40/month for. Self-hosted, zero subscription.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from .schemas import AgentTrace


# ---------------------------------------------------------------------------
# stdout sink
# ---------------------------------------------------------------------------

def stdout_sink(trace: AgentTrace) -> None:
    """Print a one-line trace summary to stderr — useful for local dev."""
    steps = len(trace.steps)
    tools = sum(len(s.tool_calls) for s in trace.steps)
    latency = trace.total_latency_ms or 0.0
    preview = (trace.last_response or "")[:80].replace("\n", " ")
    print(
        f"[trace] {trace.agent_name} | {steps} step(s) | {tools} tool(s) | "
        f"{latency:.0f}ms | {preview!r}",
        file=sys.stderr,
    )


# ---------------------------------------------------------------------------
# File sink
# ---------------------------------------------------------------------------

class FileSink:
    """
    Append every AgentTrace as a JSON line to a local file.

    Creates the parent directory if it doesn't exist.

    Args:
        path: Path to the JSONL file (e.g. "traces/my_agent.jsonl").

    Usage:
        agent = MyAgent(trace_sinks=[FileSink("traces/audit.jsonl")])
    """

    def __init__(self, path: str) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def __call__(self, trace: AgentTrace) -> None:
        with open(self._path, "a", encoding="utf-8") as fh:
            fh.write(trace.model_dump_json() + "\n")

    def __repr__(self) -> str:
        return f"FileSink(path={str(self._path)!r})"


# ---------------------------------------------------------------------------
# AgentOps sink
# ---------------------------------------------------------------------------

class AgentOpsSink:
    """
    POST every AgentTrace to a self-hosted AgentOps Console instance.

    Traces appear in the AgentOps trace viewer exactly as if the agent were
    run directly through the console. LangSmith charges $40/month for this.
    This is free, self-hosted, and requires one line of config.

    Args:
        base_url: Root URL of the AgentOps Console.
                  Default: "http://localhost:8090"
        api_key:  Optional value for the X-Ingest-Key header.
                  Required only if AGENTOPS_INGEST_KEY is set on the server.
        timeout:  HTTP timeout in seconds (default 5).
                  Failures are silenced — a dead AgentOps server never
                  breaks your agent.

    Usage:
        # Local dev
        sink = AgentOpsSink()

        # Deployed instance (Fly.io, Railway, etc.)
        sink = AgentOpsSink("https://agentops-console.fly.dev", api_key="your-key")

        agent = MyAgent(trace_sinks=[sink])
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8090",
        api_key: Optional[str] = None,
        timeout: int = 5,
    ) -> None:
        self._url = base_url.rstrip("/") + "/ingest/trace"
        self._headers = {"Content-Type": "application/json"}
        if api_key:
            self._headers["X-Ingest-Key"] = api_key
        self._timeout = timeout

    def __call__(self, trace: AgentTrace) -> None:
        import requests  # lazy import — only loaded if this sink is configured
        requests.post(
            self._url,
            data=trace.model_dump_json(),
            headers=self._headers,
            timeout=self._timeout,
        )

    def __repr__(self) -> str:
        return f"AgentOpsSink(url={self._url!r})"
