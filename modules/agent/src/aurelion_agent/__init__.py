"""
aurelion_agent — base agent loop, tool calling, and LLM provider interface

Drop-in for any Aurelion-architecture project.

    from aurelion_agent import BaseAgent, LLMProvider, tool
    from aurelion_agent import AgentTrace, AgentConfig, ToolDefinition
"""

from .base_agent import BaseAgent
from .llm_provider import LLMProvider
from .tools import tool, RegisteredTool
from .server import AgentServer
from .supervisor import SupervisorAgent
from .evaluator import AgentEvaluator, TestCase, EvalReport, EvalResult
from .sinks import FileSink, AgentOpsSink, stdout_sink
from . import builtin_tools
from .schemas import (
    AgentConfig,
    AgentStep,
    AgentTrace,
    ChatMessage,
    ConversationHistory,
    LLMProviderConfig,
    LLMProviderName,
    MessageRole,
    ToolCall,
    ToolDefinition,
    ToolResult,
)

__all__ = [
    "BaseAgent",
    "SupervisorAgent",
    "LLMProvider",
    "AgentServer",
    "AgentEvaluator",
    "TestCase",
    "EvalReport",
    "EvalResult",
    "tool",
    "RegisteredTool",
    "FileSink",
    "AgentOpsSink",
    "stdout_sink",
    "AgentConfig",
    "AgentStep",
    "AgentTrace",
    "ChatMessage",
    "ConversationHistory",
    "LLMProviderConfig",
    "LLMProviderName",
    "MessageRole",
    "ToolCall",
    "ToolDefinition",
    "ToolResult",
]
__version__ = "0.4.0"
