"""
aurelion_agent.supervisor — SupervisorAgent

Orchestrates multiple sub-agents to complete complex tasks.

Flow per respond() call:
  1. PLAN   — call LLM to decompose the task into ordered sub-agent steps
  2. EXECUTE — run each sub-agent step sequentially, collect results
  3. SYNTHESIZE — call LLM to merge all results into a coherent final answer

The full trace (plan + sub-agent steps + synthesis) is returned as an
AgentTrace so the AgentOps Console can display every step, latency,
and sub-agent involved.

Usage:
    from aurelion_agent import LLMProvider
    from aurelion_agent.supervisor import SupervisorAgent

    supervisor = SupervisorAgent(
        name="aurelion_supervisor",
        llm=LLMProvider(provider="github"),   # Claude via GitHub Models
        sub_agents={"groq": groq_agent, "gemini": gemini_agent, "ollama": ollama_agent},
    )
    trace = supervisor.respond("Research quantum computing and write a lore entry.")
    print(trace.last_response)
"""

from __future__ import annotations

import json
import re
import time
from typing import Any, Dict, List, Optional

from .base_agent import BaseAgent
from .llm_provider import LLMProvider
from .schemas import AgentStep, AgentTrace, ConversationHistory, MessageRole


class SupervisorAgent(BaseAgent):
    """
    Plans, delegates, and synthesizes across multiple sub-agents.

    Pass sub_agents as a dict mapping agent name → BaseAgent instance.
    The supervisor LLM (Claude via GitHub Models by default) decides
    which agents to use and in what order.
    """

    def __init__(
        self,
        name: str,
        llm: LLMProvider,
        sub_agents: Dict[str, BaseAgent],
        max_steps: int = 5,
    ):
        super().__init__(name=name, llm=llm)
        self.sub_agents = sub_agents
        self.max_steps = max_steps

    # ------------------------------------------------------------------
    # Required by BaseAgent
    # ------------------------------------------------------------------

    def build_system_prompt(self) -> str:
        agent_descriptions = "\n".join(
            f"  - {k}: {v.build_system_prompt()[:120].strip()}"
            for k, v in self.sub_agents.items()
        )
        return (
            "You are the Aurelion Supervisor — a strategic orchestration agent.\n"
            "Your job is to analyze tasks, plan which sub-agents to involve, and synthesize their outputs.\n\n"
            f"Available sub-agents:\n{agent_descriptions}\n\n"
            "Rules:\n"
            "- Delegate technical/code/analysis tasks to 'groq'\n"
            "- Delegate creative/story/lore/narrative tasks to 'gemini'\n"
            "- Delegate quick/simple/factual tasks to 'ollama'\n"
            "- Only involve agents that are genuinely needed\n"
            "- Be decisive and concise in your planning"
        )

    # ------------------------------------------------------------------
    # Override respond() — full supervisor loop
    # ------------------------------------------------------------------

    def respond(
        self,
        user_message: str,
        temperature: float = 0.7,
        max_tokens: int = 1500,
    ) -> AgentTrace:
        t_start = time.monotonic()
        trace = AgentTrace(agent_name=self.name)

        # ---- Step 0: Plan ----------------------------------------
        t_plan_start = time.monotonic()
        plan = self._make_plan(user_message, temperature)
        plan_latency = (time.monotonic() - t_plan_start) * 1000

        plan_step = AgentStep(
            step_index=0,
            user_input=user_message,
            context_injected="[planning]",
        )
        plan_step.final_response = (
            "Supervisor plan:\n"
            + "\n".join(f"  {i+1}. [{s['agent']}] {s['task']}" for i, s in enumerate(plan))
        )
        plan_step.latency_ms = plan_latency
        trace.add_step(plan_step)

        # ---- Steps 1..N: Execute sub-agents ----------------------
        sub_results: List[Dict[str, Any]] = []
        for i, step_def in enumerate(plan[: self.max_steps]):
            agent_name = step_def.get("agent", self._default_agent())
            task = step_def.get("task", user_message)

            agent = self.sub_agents.get(agent_name)
            if agent is None:
                # Graceful fallback to first available
                agent_name = self._default_agent()
                agent = self.sub_agents[agent_name]

            t_sub = time.monotonic()
            try:
                sub_trace = agent.respond(task, temperature=temperature, max_tokens=max_tokens)
                result_text = sub_trace.last_response
                error = None
            except Exception as exc:
                result_text = f"[agent error] {exc}"
                error = str(exc)
            sub_latency = (time.monotonic() - t_sub) * 1000

            sub_results.append({"agent": agent_name, "task": task, "result": result_text})

            sub_step = AgentStep(
                step_index=i + 1,
                user_input=task,
                context_injected=f"[delegated → {agent_name}]",
            )
            sub_step.final_response = result_text
            sub_step.latency_ms = sub_latency
            trace.add_step(sub_step)

        # ---- Final step: Synthesize --------------------------------
        t_synth = time.monotonic()
        synthesis = self._synthesize(user_message, sub_results, temperature, max_tokens)
        synth_latency = (time.monotonic() - t_synth) * 1000

        synth_step = AgentStep(
            step_index=len(plan) + 1,
            user_input=user_message,
            context_injected="[synthesis]",
        )
        synth_step.final_response = synthesis
        synth_step.latency_ms = synth_latency
        trace.add_step(synth_step)

        trace.total_latency_ms = (time.monotonic() - t_start) * 1000

        self._history.append(MessageRole.USER, user_message)
        self._history.append(MessageRole.ASSISTANT, synthesis)

        return trace

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _make_plan(self, user_message: str, temperature: float) -> List[Dict[str, str]]:
        """
        Ask the supervisor LLM to decompose the task into agent steps.
        Returns a list like: [{"agent": "groq", "task": "..."}]
        Falls back to a single step on parse failure.
        """
        available = list(self.sub_agents.keys())
        plan_prompt = (
            f"Available agents: {available}\n\n"
            f"Task: {user_message}\n\n"
            "Decide which agents to use and what specific task to give each one.\n"
            "Output ONLY valid JSON on a single line — no explanation, no markdown:\n"
            '{"steps":[{"agent":"<name>","task":"<specific instruction>"}]}\n\n'
            "Use only agents from the available list. Maximum 3 steps."
        )

        raw = self.llm.chat(
            system_prompt=self.build_system_prompt(),
            user_message=plan_prompt,
            temperature=0.3,
            max_tokens=400,
        )

        # Extract JSON — tolerant of surrounding text
        match = re.search(r'\{.*"steps"\s*:.*\}', raw, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group())
                steps = data.get("steps", [])
                if steps and isinstance(steps, list):
                    return steps
            except json.JSONDecodeError:
                pass

        # Fallback: single step with best guess agent
        return [{"agent": self._default_agent(), "task": user_message}]

    def _synthesize(
        self,
        original_task: str,
        sub_results: List[Dict[str, Any]],
        temperature: float,
        max_tokens: int,
    ) -> str:
        """
        Ask the supervisor LLM to merge all sub-agent results into a final answer.
        """
        context_blocks = "\n\n".join(
            f"[{r['agent']} — task: {r['task']}]\n{r['result']}"
            for r in sub_results
        )
        synth_prompt = (
            f"Original task: {original_task}\n\n"
            f"Sub-agent results:\n{context_blocks}\n\n"
            "Synthesize the above into a single, coherent, high-quality final answer. "
            "Integrate the best of each agent's contribution. Be clear and comprehensive."
        )

        return self.llm.chat(
            system_prompt=self.build_system_prompt(),
            user_message=synth_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def _default_agent(self) -> str:
        """Return the first available sub-agent name as a fallback."""
        return next(iter(self.sub_agents.keys()))
