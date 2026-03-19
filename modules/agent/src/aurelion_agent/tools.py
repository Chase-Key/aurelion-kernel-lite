"""
aurelion_agent.tools — @tool decorator for registering agent tools.

Usage:
    from aurelion_agent import tool

    @tool
    def search_knowledge(query: str, floor: int = 1) -> str:
        \"\"\"Search the 5-floor knowledge graph.\"\"\"
        return memory.retrieve(query, floor=floor)

    agent = MyAgent(tools=[search_knowledge])

Tools are extracted as ToolDefinition objects and dispatched automatically
when the LLM requests them via structured output or markup in its reply.
"""

import inspect
import json
from typing import Any, Callable, Dict, List, Optional, get_type_hints

from .schemas import ToolDefinition


# ---------------------------------------------------------------------------
# @tool decorator
# ---------------------------------------------------------------------------

def tool(fn: Callable = None, *, description: str = None):
    """
    Decorator that wraps a plain function into a RegisteredTool.

    Can be used bare or with a description override:

        @tool
        def my_tool(x: str) -> str: ...

        @tool(description="Override description here")
        def my_tool(x: str) -> str: ...
    """
    if fn is not None:
        # Used as @tool (no args)
        return RegisteredTool(fn, description_override=None)
    else:
        # Used as @tool(description="...")
        def decorator(f: Callable) -> "RegisteredTool":
            return RegisteredTool(f, description_override=description)
        return decorator


class RegisteredTool:
    """
    Wraps a callable and exposes it as a ToolDefinition + direct invoker.

    Returned by the @tool decorator. Pass instances directly to AgentConfig
    or BaseAgent(tools=[...]).
    """

    def __init__(self, fn: Callable, description_override: str = None):
        self._fn = fn
        self.name = fn.__name__
        self.description = description_override or (fn.__doc__ or "").strip().split("\n")[0]
        self.definition = ToolDefinition(
            name=self.name,
            description=self.description,
            parameters=self._build_param_schema(fn),
            fn=fn,
        )

    def __call__(self, **kwargs) -> Any:
        return self._fn(**kwargs)

    def invoke(self, arguments: Dict[str, Any]) -> str:
        """Call the tool with a dict of arguments. Returns str output."""
        try:
            result = self._fn(**arguments)
            return str(result)
        except Exception as exc:
            return f"[tool error] {self.name}: {exc}"

    # ------------------------------------------------------------------
    # Schema builder
    # ------------------------------------------------------------------

    @staticmethod
    def _build_param_schema(fn: Callable) -> Dict[str, Any]:
        """
        Build a minimal JSON Schema dict from function type hints.
        Covers str, int, float, bool. Everything else becomes 'string'.
        """
        type_map = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
        }
        sig = inspect.signature(fn)
        hints = {}
        try:
            hints = get_type_hints(fn)
        except Exception:
            pass

        properties: Dict[str, Any] = {}
        required: List[str] = []

        for param_name, param in sig.parameters.items():
            py_type = hints.get(param_name, str)
            json_type = type_map.get(py_type, "string")
            properties[param_name] = {"type": json_type}
            if param.default is inspect.Parameter.empty:
                required.append(param_name)

        return {
            "type": "object",
            "properties": properties,
            "required": required,
        }

    def to_openai_function(self) -> Dict[str, Any]:
        """Format for OpenAI function-calling API."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.definition.parameters,
            },
        }

    def __repr__(self) -> str:
        return f"<RegisteredTool name={self.name!r}>"


# ---------------------------------------------------------------------------
# Tool registry helpers
# ---------------------------------------------------------------------------

def build_tool_map(tools: List[Any]) -> Dict[str, RegisteredTool]:
    """
    Convert a list of @tool-decorated functions into a name→RegisteredTool map.
    Accepts both RegisteredTool instances and plain ToolDefinition objects.
    """
    registry: Dict[str, RegisteredTool] = {}
    for t in tools:
        if isinstance(t, RegisteredTool):
            registry[t.name] = t
        elif isinstance(t, ToolDefinition) and t.fn is not None:
            wrapped = RegisteredTool.__new__(RegisteredTool)
            wrapped._fn = t.fn
            wrapped.name = t.name
            wrapped.description = t.description
            wrapped.definition = t
            registry[t.name] = wrapped
    return registry


def parse_tool_calls_from_text(text: str) -> List[Dict[str, Any]]:
    """
    Parse tool calls from LLM text when native function calling is unavailable.

    Expected format in model output:
        <tool_call>{"name": "search_knowledge", "arguments": {"query": "..."}}</tool_call>

    Returns list of dicts with "name" and "arguments" keys.
    """
    import re
    pattern = r"<tool_call>(.*?)</tool_call>"
    calls = []
    for match in re.finditer(pattern, text, re.DOTALL):
        try:
            payload = json.loads(match.group(1).strip())
            if "name" in payload:
                calls.append({
                    "name": payload["name"],
                    "arguments": payload.get("arguments", {}),
                })
        except json.JSONDecodeError:
            pass
    return calls
