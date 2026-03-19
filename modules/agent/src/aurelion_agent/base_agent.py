"""
aurelion_agent.base_agent — Generic agent loop with tool calling, tracing, and async.

Subclass BaseAgent to create any character or task agent.
  - Override build_system_prompt() for agent identity/persona.
  - Override build_context() to inject memory or state per turn.
  - Pass tools=[...] (decorated with @tool) to enable tool dispatch.
  - Every respond() call returns an AgentTrace for full observability.

Sync usage:
    class MyAgent(BaseAgent):
        def build_system_prompt(self) -> str:
            return "You are a helpful assistant."

    agent = MyAgent(name="Demo", llm=LLMProvider())
    trace = agent.respond("Hello")
    print(trace.last_response)

Async usage:
    trace = await agent.arespond("Hello")
"""

from __future__ import annotations

import asyncio
import time
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Iterator, List, Optional

from .llm_provider import LLMProvider
from .schemas import (
    AgentStep, AgentTrace, ConversationHistory, MessageRole,
    ToolCall, ToolResult,
)
from .tools import RegisteredTool, build_tool_map, parse_tool_calls_from_text


class BaseAgent(ABC):
    """
    Abstract base for all Aurelion agents.

    Subclass and implement build_system_prompt(). Everything else has
    sensible defaults that you can override as needed.
    """

    def __init__(
        self,
        name: str,
        llm: LLMProvider,
        config: Optional[Dict[str, Any]] = None,
        tools: Optional[List[RegisteredTool]] = None,
        max_tool_iterations: int = 5,
        trace_sinks: Optional[List[Callable[["AgentTrace"], None]]] = None,
    ):
        self.name = name
        self.llm = llm
        self.config = config or {}
        self.max_tool_iterations = max_tool_iterations
        self._history = ConversationHistory()
        self._tool_map: Dict[str, RegisteredTool] = build_tool_map(tools or [])
        self.trace_sinks: List[Callable[[AgentTrace], None]] = list(trace_sinks or [])

    # ------------------------------------------------------------------
    # Implement in subclass
    # ------------------------------------------------------------------

    @abstractmethod
    def build_system_prompt(self) -> str:
        """Agent identity: persona, rules, tone, knowledge scope."""
        ...

    # ------------------------------------------------------------------
    # Override as needed
    # ------------------------------------------------------------------

    def build_context(self, user_message: str) -> str:
        """
        Inject dynamic context before each user turn.
        Override to pull from memory, state, retrieval, etc.
        """
        return ""

    def on_response(self, user_message: str, trace: AgentTrace) -> None:
        """
        Called after each respond() with the full trace.
        Override to write to memory, log, emit metrics, etc.
        """
        pass

    def build_tool_instructions(self) -> str:
        """
        Generate tool availability instructions appended to the system prompt.
        Override to change how tools are described to the model.
        """
        if not self._tool_map:
            return ""
        lines = [
            "\n\n## Available Tools",
            "When you need to call a tool, output ONLY this format:",
            "<tool_call>{\"name\": \"<tool_name>\", \"arguments\": {\"arg\": \"value\"}}</tool_call>",
            "\nTools:",
        ]
        for t in self._tool_map.values():
            lines.append(f"- **{t.name}**: {t.description}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Core sync loop
    # ------------------------------------------------------------------

    def respond(
        self,
        user_message: str,
        temperature: float = 0.8,
        max_tokens: int = 500,
    ) -> AgentTrace:
        """
        Send a message and return an AgentTrace with the full reasoning record.
        Automatically handles tool calls up to max_tool_iterations.
        """
        t_start = time.monotonic()
        trace = AgentTrace(agent_name=self.name)

        system_prompt = self.build_system_prompt() + self.build_tool_instructions()
        context = self.build_context(user_message)

        full_message = user_message
        if context:
            full_message = f"[Context]\n{context}\n\n[Message]\n{user_message}"

        self._history.append(MessageRole.USER, user_message)

        step = AgentStep(step_index=0, user_input=user_message, context_injected=context)
        t_step = time.monotonic()

        # Tool-calling loop
        current_message = full_message
        for iteration in range(self.max_tool_iterations):
            reply = self.llm.chat(
                system_prompt=system_prompt,
                user_message=current_message,
                history=self._history.to_dicts()[:-1],  # exclude the just-appended user msg
                temperature=temperature,
                max_tokens=max_tokens,
            )

            tool_calls = parse_tool_calls_from_text(reply)
            if not tool_calls or not self._tool_map:
                # No tool calls — final response
                step.final_response = reply
                break

            # Execute each tool call
            tool_results_text_parts = []
            for tc in tool_calls:
                tool_call = ToolCall(tool_name=tc["name"], arguments=tc.get("arguments", {}))
                step.tool_calls.append(tool_call)

                registered = self._tool_map.get(tc["name"])
                if registered:
                    output = registered.invoke(tc.get("arguments", {}))
                    result = ToolResult(tool_name=tc["name"], output=output)
                else:
                    result = ToolResult(
                        tool_name=tc["name"],
                        output="",
                        error=f"Unknown tool: {tc['name']}",
                    )
                step.tool_results.append(result)
                tool_results_text_parts.append(
                    f"[Tool: {result.tool_name}]\n{result.output or result.error}"
                )

            # Feed results back as next message.
            # Use USER role — "tool" role requires tool_call_id (native function calling).
            # Text-based <tool_call> markup does not go through native function calling.
            current_message = "\n\n".join(tool_results_text_parts)
            self._history.append(MessageRole.USER, current_message)
        else:
            # Exhausted iterations without final answer
            step.final_response = reply  # use last reply

        step.latency_ms = (time.monotonic() - t_step) * 1000
        trace.add_step(step)
        trace.total_latency_ms = (time.monotonic() - t_start) * 1000

        self._history.append(MessageRole.ASSISTANT, step.final_response)
        self.on_response(user_message, trace)
        self._emit_trace(trace)
        return trace

    # ------------------------------------------------------------------
    # Async loop
    # ------------------------------------------------------------------

    async def arespond(
        self,
        user_message: str,
        temperature: float = 0.8,
        max_tokens: int = 500,
    ) -> AgentTrace:
        """
        Async version of respond(). Runs the LLM call in a thread pool
        so it doesn't block the event loop.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self.respond(user_message, temperature, max_tokens),
        )

    # ------------------------------------------------------------------
    # Streaming respond — yields tokens as they arrive
    # ------------------------------------------------------------------

    def stream_respond(
        self,
        user_message: str,
        temperature: float = 0.8,
        max_tokens: int = 500,
    ) -> Iterator[str]:
        """
        Stream the agent's reply token-by-token.

        Yields text chunks as they arrive from the LLM. After the
        generator is fully consumed (or the last chunk received), the
        accumulated response is appended to history and on_response()
        is called — identical to respond() behaviour.

        Note: Tool calling is NOT performed during streaming. If the agent
        has tools registered, the model may describe a tool call in its
        text, but it will not be executed. Use respond() for tool dispatch.

        Usage:
            for chunk in agent.stream_respond("Tell me a story"):
                print(chunk, end="", flush=True)
            print()  # newline after stream ends

        Yields:
            str chunks (may be single characters or multi-word segments).
        """
        system_prompt = self.build_system_prompt()
        context = self.build_context(user_message)
        full_message = user_message
        if context:
            full_message = f"[Context]\n{context}\n\n[Message]\n{user_message}"

        self._history.append(MessageRole.USER, user_message)

        accumulated = []
        for chunk in self.llm.stream_chat(
            system_prompt=system_prompt,
            user_message=full_message,
            history=self._history.to_dicts()[:-1],
            temperature=temperature,
            max_tokens=max_tokens,
        ):
            accumulated.append(chunk)
            yield chunk

        full_response = "".join(accumulated)
        self._history.append(MessageRole.ASSISTANT, full_response)

        # Build a minimal trace so on_response() receives consistent info
        trace = AgentTrace(agent_name=self.name)
        step = AgentStep(step_index=0, user_input=user_message,
                         context_injected=context, final_response=full_response)
        trace.add_step(step)
        self.on_response(user_message, trace)
        self._emit_trace(trace)

    # ------------------------------------------------------------------
    # Convenience / CLI
    # ------------------------------------------------------------------

    def chat_loop(self, prompt: str = "> ", exit_command: str = "exit") -> None:
        """Interactive CLI chat loop."""
        print(f"\n--- Talking to {self.name} --- (type '{exit_command}' to quit)\n")
        while True:
            try:
                user_input = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye.")
                break
            if user_input.lower() == exit_command:
                print("Goodbye.")
                break
            if not user_input:
                continue
            trace = self.respond(user_input)
            print(f"\n{self.name}: {trace.last_response}\n")

    def _emit_trace(self, trace: AgentTrace) -> None:
        """Fire all configured trace sinks. Errors in sinks never propagate."""
        for sink in self.trace_sinks:
            try:
                sink(trace)
            except Exception:
                pass

    def reset_history(self) -> None:
        """Clear conversation history."""
        self._history = ConversationHistory()

    @property
    def history(self) -> ConversationHistory:
        return self._history

    @property
    def tools(self) -> List[str]:
        """Names of all registered tools."""
        return list(self._tool_map.keys())

    @property
    def history(self) -> List[Dict[str, str]]:
        return list(self._history)
