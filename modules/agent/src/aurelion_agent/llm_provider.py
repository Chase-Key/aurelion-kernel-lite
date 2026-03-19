"""
aurelion_agent.llm_provider — Wired LLM provider

Supports OpenAI, Anthropic Claude, and Ollama (local).
Provider selected via LLM_PROVIDER env var or constructor argument.

Usage:
    provider = LLMProvider(provider="ollama", model="llama3")
    response = provider.chat(system_prompt="You are a helpful agent.", user_message="Hello")

    # Or load from config
    from aurelion_kernel import ConfigLoader
    cfg = ConfigLoader()
    provider = LLMProvider.from_config(cfg)
"""

from typing import Iterator, List, Dict, Optional


class LLMProvider:
    """
    Wired LLM interface. Supports OpenAI, Claude, and Ollama.
    """

    SUPPORTED = ("openai", "claude", "ollama", "groq", "gemini", "github")

    def __init__(self, provider: str = "ollama", model: Optional[str] = None,
                 api_key: Optional[str] = None, base_url: Optional[str] = None):
        import os
        self.provider = provider.lower()
        # Auto-resolve api_key from env if not passed
        if api_key is None and self.provider == "github":
            api_key = os.getenv("GITHUB_TOKEN")
        self.api_key = api_key
        self.base_url = base_url or self._default_base_url(self.provider)

        if self.provider not in self.SUPPORTED:
            raise ValueError(f"Unknown provider '{provider}'. Choose from: {self.SUPPORTED}")

        # Default models per provider
        self.model = model or {
            "openai": "gpt-4o",
            "claude": "claude-3-5-sonnet-20241022",
            "ollama": "llama3.2",
            "groq": "llama-3.3-70b-versatile",
            "gemini": "gemini-2.0-flash",
            # GitHub Models marketplace — gpt-4o is available via Azure OpenAI on this endpoint
            "github": "gpt-4o",
        }[self.provider]

    @classmethod
    def from_config(cls, cfg) -> "LLMProvider":
        """Build a provider from a ConfigLoader instance."""
        provider = cfg.get("LLM_PROVIDER", "ollama")
        return cls(
            provider=provider,
            model=cfg.get("LLM_MODEL") or cfg.get("OLLAMA_MODEL"),
            api_key=cfg.get("OPENAI_API_KEY") or cfg.get("ANTHROPIC_API_KEY"),
            base_url=cfg.get("OLLAMA_BASE_URL") or cfg.get("LLM_BASE_URL"),
        )

    def chat(self, system_prompt: str, user_message: str,
             history: Optional[List[Dict]] = None,
             temperature: float = 0.8, max_tokens: int = 500) -> str:
        """
        Send a chat turn and return the assistant reply as a string.

        Args:
            system_prompt: The agent's persona/instructions.
            user_message: The latest user input.
            history: Optional prior turns as [{"role": "user"|"assistant", "content": "..."}].
            temperature: Creativity dial.
            max_tokens: Max reply length.
        """
        if self.provider in ("openai", "groq", "gemini", "github"):
            return self._chat_openai(system_prompt, user_message, history, temperature, max_tokens)
        elif self.provider == "claude":
            return self._chat_claude(system_prompt, user_message, history, temperature, max_tokens)
        elif self.provider == "ollama":
            return self._chat_ollama(system_prompt, user_message, history, temperature, max_tokens)

    # ------------------------------------------------------------------
    # OpenAI
    # ------------------------------------------------------------------

    def _chat_openai(self, system_prompt, user_message, history, temperature, max_tokens) -> str:
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key, base_url=self.base_url or None)
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    # ------------------------------------------------------------------
    # Anthropic Claude
    # ------------------------------------------------------------------

    def _chat_claude(self, system_prompt, user_message, history, temperature, max_tokens) -> str:
        from anthropic import Anthropic
        client = Anthropic(api_key=self.api_key)
        messages = []
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        response = client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages,
        )
        return response.content[0].text

    # ------------------------------------------------------------------
    # Ollama (local)
    # ------------------------------------------------------------------

    def _chat_ollama(self, system_prompt, user_message, history, temperature, max_tokens) -> str:
        import requests
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }
        response = requests.post(f"{self.base_url}/api/chat", json=payload, timeout=120)
        response.raise_for_status()
        return response.json()["message"]["content"]

    # ------------------------------------------------------------------
    # Streaming — yields text tokens as the model generates them
    # ------------------------------------------------------------------

    def stream_chat(
        self,
        system_prompt: str,
        user_message: str,
        history: Optional[List[Dict]] = None,
        temperature: float = 0.8,
        max_tokens: int = 500,
    ) -> Iterator[str]:
        """
        Stream an LLM response token-by-token.

        Yields string chunks as they arrive from the model.
        Accumulate them yourself if you need the full response:
            full = "".join(provider.stream_chat(...))

        Args:
            system_prompt: Agent identity/instructions.
            user_message: Current user input.
            history: Prior turns as list of {"role": ..., "content": ...}.
            temperature: Creativity dial.
            max_tokens: Max reply length.

        Yields:
            str chunks (may be single characters, words, or sentences
            depending on the provider's chunking behaviour).
        """
        if self.provider in ("openai", "groq", "gemini", "github"):
            yield from self._stream_openai(system_prompt, user_message, history, temperature, max_tokens)
        elif self.provider == "claude":
            yield from self._stream_claude(system_prompt, user_message, history, temperature, max_tokens)
        elif self.provider == "ollama":
            yield from self._stream_ollama(system_prompt, user_message, history, temperature, max_tokens)

    def _stream_openai(self, system_prompt, user_message, history, temperature, max_tokens) -> Iterator[str]:
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key, base_url=self.base_url or None)
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        stream = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    def _stream_claude(self, system_prompt, user_message, history, temperature, max_tokens) -> Iterator[str]:
        from anthropic import Anthropic
        client = Anthropic(api_key=self.api_key)
        messages = []
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        with client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                yield text

    def _stream_ollama(self, system_prompt, user_message, history, temperature, max_tokens) -> Iterator[str]:
        import json
        import requests
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }
        with requests.post(
            f"{self.base_url}/api/chat", json=payload, stream=True, timeout=120
        ) as resp:
            resp.raise_for_status()
            for raw_line in resp.iter_lines():
                if not raw_line:
                    continue
                data = json.loads(raw_line)
                delta = data.get("message", {}).get("content", "")
                if delta:
                    yield delta
                if data.get("done"):
                    break

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _default_base_url(provider: str) -> str:
        return {
            "openai": "https://api.openai.com/v1",
            "claude": "https://api.anthropic.com",
            "ollama": "http://localhost:11434",
            "groq": "https://api.groq.com/openai/v1",
            "gemini": "https://generativelanguage.googleapis.com/v1beta/openai/",
            "github": "https://models.inference.ai.azure.com",
        }.get(provider, "")
