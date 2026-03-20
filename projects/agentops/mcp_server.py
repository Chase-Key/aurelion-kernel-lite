"""
mcp_server.py — AgentOps Console MCP Server

Exposes the AgentOps agent console as MCP tools.
AI assistants (VS Code Copilot, Claude Desktop, Cursor) can run agents,
compare outputs, and inspect traces directly from chat — no browser needed.

Tools exposed
-------------
list_agents()                    List all registered agents with provider/model info
run_agent(agent, message)        Run a prompt through a named agent, get the response
compare_agents(message)          Run the same prompt through all agents in parallel
get_traces(limit)                List recent agent runs (newest first)
get_trace(run_id)                Get full trace detail for a specific run

Setup — VS Code Copilot (add to .vscode/mcp.json in aurelion-eco)
------------------------------------------------------------------
{
  "servers": {
    "agentops": {
      "type": "stdio",
      "command": "${workspaceFolder}/.venv/Scripts/python.exe",
      "args": ["${workspaceFolder}/projects/agentops/mcp_server.py"]
    }
  }
}

Requirements
------------
pip install mcp  (already in the aurelion-eco venv)
"""

from __future__ import annotations

import io
import json
import os
import sys
import uuid
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Add agentops project directory to path so registry/models are importable
# ---------------------------------------------------------------------------
_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))

# Load .env (same as agentops main.py)
from dotenv import load_dotenv  # noqa: E402

load_dotenv(dotenv_path=_HERE / ".env")

# ---------------------------------------------------------------------------
# MCP server setup
# ---------------------------------------------------------------------------
from mcp.server.fastmcp import FastMCP  # noqa: E402

mcp = FastMCP(
    "agentops",
    instructions=(
        "You have access to the AgentOps agent console. "
        "Use list_agents() to see what AI agents are available, then "
        "run_agent(agent, message) to get a response from any agent. "
        "Use compare_agents(message) to run the same prompt through all agents "
        "and compare outputs side by side. "
        "Use get_traces() and get_trace(run_id) to inspect past runs."
    ),
)


# ---------------------------------------------------------------------------
# Tool: list_agents
# ---------------------------------------------------------------------------

@mcp.tool()
def list_agents() -> str:
    """
    List all registered agents in the AgentOps console.

    Returns a JSON array. Each entry has:
      name      Agent identifier (use this in run_agent)
      provider  LLM provider (groq, openai, ollama, gemini, claude)
      model     Specific model name
      tools     Number of tools registered on the agent
    """
    from registry import list_agents as _list

    result = _list()
    return json.dumps(result, indent=2)


# ---------------------------------------------------------------------------
# Tool: run_agent
# ---------------------------------------------------------------------------

@mcp.tool()
def run_agent(agent: str, message: str) -> str:
    """
    Run a prompt through a named agent and return its response.

    The run is saved to the AgentOps trace database automatically.

    Args:
        agent:   Agent name from list_agents() (e.g. "groq", "openai", "ollama")
        message: The prompt to send to the agent

    Returns:
        JSON with keys:
          run_id       Unique run identifier (use with get_trace for full detail)
          agent        Name of the agent that ran
          provider     LLM provider used
          model        Specific model used
          response     The agent's reply
          latency_ms   How long the LLM call took
          tool_calls   Number of tool calls made during this run
    """
    from database import SessionLocal
    from models import MemoryRecord, RunRecord
    from registry import get_agent

    try:
        agent_obj = get_agent(agent)
    except KeyError:
        available = json.loads(list_agents())
        return json.dumps({
            "error": f"Agent '{agent}' not found.",
            "available_agents": [a["name"] for a in available],
        })

    buf = io.StringIO()
    try:
        with redirect_stdout(buf), redirect_stderr(buf):
            trace = agent_obj.respond(message)
    except Exception as exc:
        return json.dumps({"error": f"Agent error: {exc}"})

    run_id = str(uuid.uuid4())
    tool_count = sum(len(s.tool_calls) for s in trace.steps)

    db = SessionLocal()
    try:
        record = RunRecord(
            run_id=run_id,
            agent_name=trace.agent_name,
            user_message=message,
            final_response=trace.last_response,
            provider=agent_obj.llm.provider,
            model=agent_obj.llm.model,
            total_latency_ms=trace.total_latency_ms or 0.0,
            tool_calls_count=tool_count,
            created_at=datetime.now(timezone.utc),
            trace_json=trace.model_dump_json(),
        )
        db.add(record)
        # Auto-save to memory
        mem = MemoryRecord(
            agent_name=trace.agent_name,
            content=f"Q: {message[:150]} | A: {(trace.last_response or '')[:300]}",
            tags=f"conversation,{trace.agent_name},mcp",
            source_run_id=run_id,
        )
        db.add(mem)
        db.commit()
    finally:
        db.close()

    return json.dumps({
        "run_id": run_id,
        "agent": trace.agent_name,
        "provider": agent_obj.llm.provider,
        "model": agent_obj.llm.model,
        "response": trace.last_response,
        "latency_ms": round(trace.total_latency_ms or 0.0, 1),
        "tool_calls": tool_count,
    }, indent=2)


# ---------------------------------------------------------------------------
# Tool: compare_agents
# ---------------------------------------------------------------------------

@mcp.tool()
def compare_agents(message: str) -> str:
    """
    Run the same prompt through all available agents in parallel.

    Each agent runs concurrently. All results are saved as traces.
    This is the fastest way to compare different LLM providers side by side
    without opening the browser.

    Args:
        message: The prompt to send to every agent

    Returns:
        JSON array — one entry per agent, same structure as run_agent().
        Failed agents include an "error" key instead of "response".
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from registry import list_agents as _list

    agents_info = _list()
    # Skip supervisor / unified meta-agents for raw comparison
    target_names = [a["name"] for a in agents_info if a["name"] not in ("supervisor", "unified")]

    def _run_one(name: str) -> dict:
        result_str = run_agent(name, message)
        return json.loads(result_str)

    results = []
    with ThreadPoolExecutor(max_workers=len(target_names)) as pool:
        futures = {pool.submit(_run_one, name): name for name in target_names}
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as exc:
                results.append({"agent": futures[future], "error": str(exc)})

    results.sort(key=lambda r: r.get("latency_ms", 9999))
    return json.dumps(results, indent=2)


# ---------------------------------------------------------------------------
# Tool: get_traces
# ---------------------------------------------------------------------------

@mcp.tool()
def get_traces(limit: int = 20) -> str:
    """
    List recent agent runs from the AgentOps trace database.

    Args:
        limit: Maximum number of traces to return (default 20, max 100)

    Returns:
        JSON array, newest runs first. Each entry has:
          run_id       Use with get_trace() for full detail
          agent        Which agent ran
          provider     LLM provider
          model        Specific model
          message      First 80 chars of the input prompt
          latency_ms   How long the run took
          tool_calls   Number of tool calls made
          created_at   ISO 8601 timestamp
    """
    from database import SessionLocal
    from models import RunRecord

    limit = max(1, min(limit, 100))
    db = SessionLocal()
    try:
        rows = (
            db.query(RunRecord)
            .order_by(RunRecord.created_at.desc())
            .limit(limit)
            .all()
        )
        result = []
        for r in rows:
            msg = str(r.user_message or "")
            result.append({
                "run_id": r.run_id,
                "agent": r.agent_name,
                "provider": r.provider,
                "model": r.model,
                "message": msg[:80] + ("…" if len(msg) > 80 else ""),
                "latency_ms": round(float(r.total_latency_ms or 0), 1),
                "tool_calls": r.tool_calls_count or 0,
                "created_at": r.created_at.isoformat() if r.created_at else None,
            })
        return json.dumps(result, indent=2)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Tool: get_trace
# ---------------------------------------------------------------------------

@mcp.tool()
def get_trace(run_id: str) -> str:
    """
    Get the full trace for a specific agent run.

    Args:
        run_id: The run_id from get_traces() or run_agent()

    Returns:
        Full trace JSON including every step, tool call, tool result,
        context injected, and the final response. Returns an error object
        if the run_id is not found.
    """
    from database import SessionLocal
    from models import RunRecord

    db = SessionLocal()
    try:
        row = db.query(RunRecord).filter(RunRecord.run_id == run_id).first()
        if not row:
            return json.dumps({"error": f"Run '{run_id}' not found."})

        return json.dumps({
            "run_id": row.run_id,
            "agent": row.agent_name,
            "provider": row.provider,
            "model": row.model,
            "message": row.user_message,
            "response": row.final_response,
            "latency_ms": round(float(row.total_latency_ms or 0), 1),
            "tool_calls": row.tool_calls_count or 0,
            "created_at": row.created_at.isoformat() if row.created_at else None,
            "trace": json.loads(str(row.trace_json)) if row.trace_json else None,
        }, indent=2, default=str)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
