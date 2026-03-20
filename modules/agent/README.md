# aurelion-agent

**Part of the [AURELION Ecosystem](https://github.com/aurelion-labs/aurelion-eco)**

A modular base agent loop with tool calling, multi-provider LLM support, and built-in trace observability. Drop it into any project to get a production-ready agent in minutes.

## Install

```bash
pip install aurelion-agent
```

## Quickstart

```python
from aurelion_agent import BaseAgent, LLMProvider

class MyAgent(BaseAgent):
    name = "my-agent"
    system_prompt = "You are a helpful assistant."

agent = MyAgent(llm=LLMProvider(provider="groq", model="llama-3.3-70b-versatile"))
trace = agent.respond("What is data minimisation?")
print(trace.last_response)
```

## Providers

Supports: `groq`, `openai`, `anthropic` (claude), `ollama`, `gemini`, `mistral`

```python
LLMProvider(provider="openai", model="gpt-4o")
LLMProvider(provider="ollama", model="llama3")
LLMProvider(provider="anthropic", model="claude-3-5-sonnet-20241022")
```

## Trace Sinks

Wire observability into any agent with built-in sinks:

```python
from aurelion_agent import FileSink, AgentOpsSink, stdout_sink

agent = MyAgent(
    llm=LLMProvider(provider="groq"),
    trace_sinks=[
        stdout_sink,
        FileSink("traces.jsonl"),
        AgentOpsSink("https://your-agentops-instance.fly.dev", api_key="..."),
    ]
)
```

## Tool Calling

```python
from aurelion_agent import BaseAgent, LLMProvider, tool

class ResearchAgent(BaseAgent):
    name = "researcher"
    system_prompt = "You research topics thoroughly."

    @tool
    def search_web(self, query: str) -> str:
        """Search the web for information."""
        # your implementation
        return results
```

## Architecture

`aurelion-agent` is the Agent module of the AURELION modular cognitive architecture:

```
KERNEL    → Knowledge schema and organizational structure
MEMORY    → Persistent storage and retrieval
NEXUS     → Agent orchestration and routing
ADVISOR   → Strategic planning and knowledge management
AGENT     → This package — AI collaboration and prompt protocols
```

## Links

- GitHub: [aurelion-labs/aurelion-eco](https://github.com/aurelion-labs/aurelion-eco)
- Ecosystem: [AURELION Ecosystem](https://github.com/aurelion-labs/aurelion-eco/blob/master/README.md)
