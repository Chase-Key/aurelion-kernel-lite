"""
aurelion_agent.schemas — Pydantic models for the agent layer.

All data flowing into or out of agents, tools, and the LLM provider
is typed here. Import these anywhere you need validated structures.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Callable
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class LLMProviderName(str, Enum):
    OPENAI = "openai"
    CLAUDE = "claude"
    OLLAMA = "ollama"


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


# ---------------------------------------------------------------------------
# Config models
# ---------------------------------------------------------------------------

class LLMProviderConfig(BaseModel):
    """Typed configuration for an LLM provider."""
    provider: LLMProviderName = LLMProviderName.OLLAMA
    model: Optional[str] = None
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = Field(default=0.8, ge=0.0, le=2.0)
    max_tokens: int = Field(default=500, gt=0)


class ToolDefinition(BaseModel):
    """Schema for a registered tool that an agent can call."""
    name: str
    description: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    # The actual callable — excluded from serialization
    fn: Any = Field(default=None, exclude=True)

    model_config = {"arbitrary_types_allowed": True}


class AgentConfig(BaseModel):
    """Full configuration for a BaseAgent instance."""
    name: str
    llm: LLMProviderConfig = Field(default_factory=LLMProviderConfig)
    tools: List[ToolDefinition] = Field(default_factory=list)
    max_tool_iterations: int = Field(default=5, gt=0)
    settings: Dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Message / history models
# ---------------------------------------------------------------------------

class ChatMessage(BaseModel):
    """A single message in a conversation."""
    role: MessageRole
    content: str
    tool_name: Optional[str] = None  # populated for role=tool responses


class ConversationHistory(BaseModel):
    """Ordered list of messages in a session."""
    messages: List[ChatMessage] = Field(default_factory=list)

    def append(self, role: MessageRole, content: str,
               tool_name: Optional[str] = None) -> None:
        self.messages.append(
            ChatMessage(role=role, content=content, tool_name=tool_name)
        )

    def to_dicts(self) -> List[Dict[str, str]]:
        """Convert to the raw dict format expected by LLM APIs."""
        return [{"role": m.role.value, "content": m.content}
                for m in self.messages]


# ---------------------------------------------------------------------------
# Tool call / result models
# ---------------------------------------------------------------------------

class ToolCall(BaseModel):
    """A tool invocation requested by the agent."""
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """The result of executing a tool."""
    tool_name: str
    output: str
    error: Optional[str] = None

    @property
    def success(self) -> bool:
        return self.error is None


# ---------------------------------------------------------------------------
# Trace models (observability)
# ---------------------------------------------------------------------------

class AgentStep(BaseModel):
    """One step in an agent's reasoning trace."""
    step_index: int
    user_input: str
    context_injected: str = ""
    tool_calls: List[ToolCall] = Field(default_factory=list)
    tool_results: List[ToolResult] = Field(default_factory=list)
    final_response: str = ""
    latency_ms: Optional[float] = None


class AgentTrace(BaseModel):
    """Full trace of a single agent.respond() call."""
    agent_name: str
    steps: List[AgentStep] = Field(default_factory=list)
    total_latency_ms: Optional[float] = None

    def add_step(self, step: AgentStep) -> None:
        self.steps.append(step)

    @property
    def last_response(self) -> str:
        if self.steps:
            raw = self.steps[-1].final_response
            # Strip any unexecuted <tool_call> markup that bled into the final reply
            # (happens when max_tool_iterations is exhausted or parsing fails)
            import re
            cleaned = re.sub(r"<tool_call>.*?</tool_call>", "", raw, flags=re.DOTALL)
            # Also strip non-standard tool-output tags some local models emit, e.g.
            # <calculate {...}>204</calculate>
            cleaned = re.sub(r"<[a-z_][a-z0-9_]*\s*[^>]*>.*?</[a-z_][a-z0-9_]*>",
                             "", cleaned, flags=re.DOTALL)
            cleaned = cleaned.strip()
            return cleaned if cleaned else raw
        return ""
