"""
AgentOps Console — FastAPI backend.

Endpoints:
  GET  /              → serve the console UI
  GET  /health        → health check
  GET  /agents        → list registered agents
  POST /run           → run a task through an agent, save trace to DB
  POST /compare       → run same prompt through multiple agents in parallel
  POST /workflow/run  → linear pipeline (agent-A → agent-B → ...)
  GET  /memory        → list saved memories
  POST /memory        → manually save a memory
  DELETE /memory/{id} → delete a memory
  GET  /traces        → list recent runs (most recent first)
  GET  /traces/{id}   → full trace detail for a single run

Run:
  uvicorn main:app --reload --port 8090
"""
from __future__ import annotations

import hmac
import json
import os
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import List, Optional

from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from gate import DemoGate, handle_login, login_page, _COOKIE
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import RunRecord, MemoryRecord
from registry import get_agent, list_agents

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AgentOps Console", version="0.1.0")
app.add_middleware(DemoGate)
app.mount("/static", StaticFiles(directory="static"), name="static")


# ---------------------------------------------------------------------------
# Request/Response schemas
# ---------------------------------------------------------------------------

class RunRequest(BaseModel):
    agent: str
    message: str


class CompareRequest(BaseModel):
    message: str
    agents: Optional[List[str]] = None  # None = all non-supervisor agents


class WorkflowStep(BaseModel):
    agent: str
    prompt: Optional[str] = None  # if None, passes previous output as the prompt


class WorkflowRequest(BaseModel):
    steps: List[WorkflowStep]
    initial_prompt: str
    session_name: Optional[str] = None


class MemorySaveRequest(BaseModel):
    content: str
    tags: str = ""
    agent_name: str = "manual"


class RunResponse(BaseModel):
    run_id: str
    agent: str
    provider: str
    model: str
    response: str
    latency_ms: float
    tool_calls: int


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/login", response_class=HTMLResponse)
def show_login():
    return login_page()


@app.post("/login")
async def do_login(request: Request):
    return await handle_login(request)


@app.get("/logout")
def logout():
    resp = RedirectResponse("/login", status_code=302)
    resp.delete_cookie(_COOKIE)
    return resp


@app.get("/", response_class=HTMLResponse)
def console():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
def health():
    return {"status": "ok", "service": "agentops-console"}


@app.get("/setup")
def setup_status():
    """
    Returns configuration status for every supported provider.
    Used by the Setup tab to guide users through first-run key configuration.
    """
    import os

    def _hint(val: str | None) -> str | None:
        """Return a safe prefix hint like 'gsk_••••' so users can confirm the right key."""
        if not val:
            return None
        visible = val[:6] if len(val) >= 6 else val
        return f"{visible}{'•' * min(4, max(0, len(val) - 6))}"

    providers = [
        {
            "name": "groq",
            "label": "Groq",
            "description": "Llama 3.3 70B — fast, free, great for code & analysis",
            "configured": bool(os.getenv("GROQ_API_KEY")),
            "key_hint": _hint(os.getenv("GROQ_API_KEY")),
            "free": True,
            "local": False,
            "key_var": "GROQ_API_KEY",
            "signup_url": "https://console.groq.com/keys",
            "agents": ["groq"],
        },
        {
            "name": "gemini",
            "label": "Google Gemini",
            "description": "Gemini 2.0 Flash — free, great for creative & lore",
            "configured": bool(os.getenv("GEMINI_API_KEY")),
            "key_hint": _hint(os.getenv("GEMINI_API_KEY")),
            "free": True,
            "local": False,
            "key_var": "GEMINI_API_KEY",
            "signup_url": "https://aistudio.google.com/apikey",
            "agents": ["gemini"],
        },
        {
            "name": "github",
            "label": "GitHub Copilot",
            "description": "GPT-4o + Mistral Large — free with Copilot subscription",
            "configured": bool(os.getenv("GITHUB_TOKEN")),
            "key_hint": _hint(os.getenv("GITHUB_TOKEN")),
            "free": True,
            "local": False,
            "key_var": "GITHUB_TOKEN",
            "requires": "GitHub Copilot subscription",
            "signup_url": "https://github.com/settings/tokens",
            "agents": ["claude", "mistral"],
        },
        {
            "name": "openai",
            "label": "OpenAI",
            "description": "GPT-4o — best generalist, pay-per-use (~$0.01/run)",
            "configured": bool(os.getenv("OPENAI_API_KEY")),
            "key_hint": _hint(os.getenv("OPENAI_API_KEY")),
            "free": False,
            "local": False,
            "key_var": "OPENAI_API_KEY",
            "signup_url": "https://platform.openai.com/api-keys",
            "agents": ["openai"],
        },
        {
            "name": "ollama",
            "label": "Ollama",
            "description": "Local Llama 3.2 — completely offline, no key needed",
            "configured": True,
            "key_hint": None,
            "free": True,
            "local": True,
            "key_var": None,
            "note": "Requires Ollama running locally: ollama pull llama3.2",
            "signup_url": "https://ollama.ai/download",
            "agents": ["ollama"],
        },
    ]

    paid_keys = [p for p in providers if not p["free"] and not p["local"]]
    free_keys = [p for p in providers if p["free"] and not p["local"]]
    configured_free = sum(1 for p in free_keys if p["configured"])
    configured_any = any(p["configured"] for p in providers if not p["local"])

    return {
        "providers": providers,
        "configured_free": configured_free,
        "total_free": len(free_keys),
        "has_any_key": configured_any,
        "fully_configured": all(p["configured"] for p in providers),
        "version": "0.1.0",
    }


@app.get("/agents")
def agents_list():
    return list_agents()


@app.post("/run", response_model=RunResponse)
def run_task(req: RunRequest, db: Session = Depends(get_db)):
    try:
        agent = get_agent(req.agent)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        trace = agent.respond(req.message)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Agent error ({req.agent}): {e}")

    run_id = str(uuid.uuid4())
    tool_count = sum(len(s.tool_calls) for s in trace.steps)

    record = RunRecord(
        run_id=run_id,
        agent_name=trace.agent_name,
        user_message=req.message,
        final_response=trace.last_response,
        provider=agent.llm.provider,
        model=agent.llm.model,
        total_latency_ms=trace.total_latency_ms or 0.0,
        tool_calls_count=tool_count,
        created_at=datetime.now(timezone.utc),
        trace_json=trace.model_dump_json(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    # Auto-save conversation to memory (summary, not full response — keeps memory lean)
    mem = MemoryRecord(
        agent_name=trace.agent_name,
        content=f"Q: {req.message[:150]} | A: {(trace.last_response or '')[:300]}",
        tags=f"conversation,{trace.agent_name}",
        source_run_id=run_id,
    )
    db.add(mem)
    db.commit()

    return RunResponse(
        run_id=run_id,
        agent=trace.agent_name,
        provider=agent.llm.provider,
        model=agent.llm.model,
        response=trace.last_response,
        latency_ms=trace.total_latency_ms or 0.0,
        tool_calls=tool_count,
    )


@app.post("/compare")
def compare_agents(req: CompareRequest):
    """Run the same prompt through multiple agents in parallel and return all results."""
    all_agent_names = [a["name"] for a in list_agents() if a["name"] not in ("supervisor", "unified")]
    target_names = req.agents if req.agents else all_agent_names

    def _run_one(name: str) -> dict:
        from database import SessionLocal
        db = SessionLocal()
        try:
            agent = get_agent(name)
            trace = agent.respond(req.message)
            tool_count = sum(len(s.tool_calls) for s in trace.steps)
            run_id = str(uuid.uuid4())
            record = RunRecord(
                run_id=run_id,
                agent_name=trace.agent_name,
                user_message=req.message,
                final_response=trace.last_response,
                provider=agent.llm.provider,
                model=agent.llm.model,
                total_latency_ms=trace.total_latency_ms or 0.0,
                tool_calls_count=tool_count,
                created_at=datetime.now(timezone.utc),
                trace_json=trace.model_dump_json(),
            )
            db.add(record)
            db.commit()
            return {
                "agent": name,
                "provider": agent.llm.provider,
                "model": agent.llm.model,
                "response": trace.last_response,
                "latency_ms": round(trace.total_latency_ms or 0.0, 1),
                "tool_calls": tool_count,
                "run_id": run_id,
                "error": None,
            }
        except Exception as e:
            return {
                "agent": name,
                "provider": "?",
                "model": "?",
                "response": "",
                "latency_ms": 0,
                "tool_calls": 0,
                "run_id": None,
                "error": str(e),
            }
        finally:
            db.close()

    results = []
    with ThreadPoolExecutor(max_workers=len(target_names)) as executor:
        future_map = {executor.submit(_run_one, n): n for n in target_names}
        for future in as_completed(future_map):
            results.append(future.result())

    # Return in consistent order matching target_names
    order = {n: i for i, n in enumerate(target_names)}
    results.sort(key=lambda r: order.get(r["agent"], 99))
    return results


# ---------------------------------------------------------------------------
# Workflow — linear pipeline
# ---------------------------------------------------------------------------

@app.post("/workflow/run")
def run_workflow(req: WorkflowRequest, db: Session = Depends(get_db)):
    """
    Run a linear agent pipeline. Each step receives the previous step's output
    as its input (unless the step has its own prompt override).
    Returns a list of step results plus the final output.
    """
    if not req.steps:
        raise HTTPException(status_code=400, detail="steps cannot be empty")

    session_id = str(uuid.uuid4())
    step_results = []
    current_input = req.initial_prompt

    for i, step_def in enumerate(req.steps):
        agent_name = step_def.agent
        step_prompt = step_def.prompt or current_input

        try:
            agent = get_agent(agent_name)
        except KeyError as e:
            raise HTTPException(status_code=404, detail=str(e))

        try:
            trace = agent.respond(step_prompt)
        except Exception as e:
            step_results.append({
                "step": i + 1,
                "agent": agent_name,
                "input": step_prompt,
                "output": "",
                "latency_ms": 0,
                "tool_calls": 0,
                "run_id": None,
                "error": str(e),
            })
            break  # stop pipeline on error

        tool_count = sum(len(s.tool_calls) for s in trace.steps)
        run_id = str(uuid.uuid4())
        record = RunRecord(
            run_id=run_id,
            agent_name=f"workflow:{agent_name}",
            user_message=step_prompt,
            final_response=trace.last_response,
            provider=agent.llm.provider,
            model=agent.llm.model,
            total_latency_ms=trace.total_latency_ms or 0.0,
            tool_calls_count=tool_count,
            created_at=datetime.now(timezone.utc),
            trace_json=trace.model_dump_json(),
        )
        db.add(record)

        step_results.append({
            "step": i + 1,
            "agent": agent_name,
            "input": step_prompt,
            "output": trace.last_response,
            "latency_ms": round(trace.total_latency_ms or 0.0, 1),
            "tool_calls": tool_count,
            "run_id": run_id,
            "error": None,
        })
        current_input = trace.last_response  # chain output → next input

    db.commit()

    # Auto-save the workflow session as a memory
    if step_results and not step_results[-1].get("error"):
        mem = MemoryRecord(
            agent_name="workflow",
            content=(
                f"[Session: {req.session_name or session_id[:8]}] "
                f"Pipeline: {' → '.join(s.agent for s in req.steps)} | "
                f"Prompt: {req.initial_prompt[:120]} | "
                f"Result: {step_results[-1]['output'][:200]}"
            ),
            tags=f"workflow,{','.join(s.agent for s in req.steps)}",
            source_run_id=session_id,
        )
        db.add(mem)
        db.commit()

    total_latency = sum(s.get("latency_ms", 0) for s in step_results)
    return {
        "session_id": session_id,
        "session_name": req.session_name,
        "steps": step_results,
        "final_output": step_results[-1]["output"] if step_results else "",
        "total_latency_ms": round(total_latency, 1),
    }


# ---------------------------------------------------------------------------
# Memory — persistent memory CRUD
# ---------------------------------------------------------------------------

@app.get("/memory")
def list_memories(limit: int = 50, agent: Optional[str] = None, q: Optional[str] = None,
                  db: Session = Depends(get_db)):
    query = db.query(MemoryRecord).order_by(MemoryRecord.created_at.desc())
    if agent:
        query = query.filter(MemoryRecord.agent_name == agent)
    rows = query.limit(500).all()
    if q:
        ql = q.lower()
        rows = [r for r in rows if ql in (r.content or "").lower() or ql in (r.tags or "").lower()]
    rows = rows[:limit]
    return [
        {
            "memory_id": r.memory_id,
            "agent": r.agent_name,
            "content": r.content,
            "tags": r.tags,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]


@app.post("/memory", status_code=201)
def save_memory_manual(req: MemorySaveRequest, db: Session = Depends(get_db)):
    record = MemoryRecord(
        agent_name=req.agent_name,
        content=req.content,
        tags=req.tags,
    )
    db.add(record)
    db.commit()
    return {"memory_id": record.memory_id, "saved": True}


@app.delete("/memory/{memory_id}")
def delete_memory(memory_id: str, db: Session = Depends(get_db)):
    row = db.query(MemoryRecord).filter(MemoryRecord.memory_id == memory_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Memory not found")
    db.delete(row)
    db.commit()
    return {"deleted": memory_id}


@app.get("/traces")
def list_traces(limit: int = 100, agent: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(RunRecord).order_by(RunRecord.created_at.desc())
    if agent:
        q = q.filter(RunRecord.agent_name == agent)
    rows = q.limit(limit).all()
    return [
        {
            "run_id": r.run_id,
            "agent": r.agent_name,
            "provider": r.provider,
            "model": r.model,
            "message": r.user_message[:80] + ("…" if len(r.user_message or "") > 80 else ""),
            "latency_ms": round(r.total_latency_ms or 0, 1),
            "tool_calls": r.tool_calls_count or 0,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]


@app.get("/traces/{run_id}")
def get_trace(run_id: str, db: Session = Depends(get_db)):
    row = db.query(RunRecord).filter(RunRecord.run_id == run_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Run not found")
    return {
        "run_id": row.run_id,
        "agent": row.agent_name,
        "provider": row.provider,
        "model": row.model,
        "message": row.user_message,
        "response": row.final_response,
        "latency_ms": round(row.total_latency_ms or 0, 1),
        "tool_calls": row.tool_calls_count or 0,
        "created_at": row.created_at.isoformat() if row.created_at else None,
        "trace": json.loads(row.trace_json) if row.trace_json else None,
    }

# ---------------------------------------------------------------------------
# External trace ingestion — POST /ingest/trace
# ---------------------------------------------------------------------------
# Any agent that extends BaseAgent and configures an AgentOpsSink will POST
# its traces here automatically. This is the self-hosted alternative to
# LangSmith / Langfuse / Helicone — zero subscription required.
#
# Security: set AGENTOPS_INGEST_KEY in your environment / Fly secrets.
# If the env var is not set, the endpoint accepts all traffic (local dev).
# If set, callers must include:  X-Ingest-Key: <value>
# ---------------------------------------------------------------------------

class _TraceStepPayload(BaseModel):
    step_index: int = 0
    user_input: str = ""
    context_injected: str = ""
    tool_calls: List[dict] = []
    tool_results: List[dict] = []
    final_response: str = ""
    latency_ms: Optional[float] = None


class IngestTraceRequest(BaseModel):
    """Matches aurelion_agent.schemas.AgentTrace — no import dependency needed."""
    agent_name: str
    steps: List[_TraceStepPayload] = []
    total_latency_ms: Optional[float] = None
    # Optional: caller can annotate the source (provider/model) for display
    provider: Optional[str] = None
    model: Optional[str] = None


@app.post("/ingest/trace", status_code=202)
def ingest_trace(
    payload: IngestTraceRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Accept an AgentTrace from any external agent configured with AgentOpsSink.

    Returns 202 Accepted so sinks can fire-and-forget without waiting.
    Authentication: X-Ingest-Key header, validated against AGENTOPS_INGEST_KEY
    env var (constant-time comparison). If env var is unset, all traffic is
    accepted (appropriate for local / private deployments).
    """
    ingest_key = os.getenv("AGENTOPS_INGEST_KEY", "")
    if ingest_key:
        provided = request.headers.get("X-Ingest-Key", "")
        if not hmac.compare_digest(ingest_key.encode(), provided.encode()):
            raise HTTPException(status_code=401, detail="Invalid or missing X-Ingest-Key")

    user_message = payload.steps[0].user_input if payload.steps else ""
    final_response = payload.steps[-1].final_response if payload.steps else ""
    tool_count = sum(len(s.tool_calls) for s in payload.steps)
    run_id = str(uuid.uuid4())

    record = RunRecord(
        run_id=run_id,
        agent_name=payload.agent_name,
        user_message=user_message,
        final_response=final_response,
        provider=payload.provider or "external",
        model=payload.model or "external",
        total_latency_ms=payload.total_latency_ms or 0.0,
        tool_calls_count=tool_count,
        created_at=datetime.now(timezone.utc),
        trace_json=payload.model_dump_json(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return {"run_id": run_id, "status": "accepted", "agent": payload.agent_name}