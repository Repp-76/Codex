from .base import AIProvider
from .http_utils import openai_style_chat


class OpenRouterProvider(AIProvider):
    name = "openrouter"
    default_model = "openai/gpt-4o-mini"

    def chat(self, messages, model, temperature, max_tokens):
        return openai_style_chat(
            "https://openrouter.ai/api/v1/chat/completions",
            self.api_key, messages, model, temperature, max_tokens,
            self.name, self.default_model,
            extra_headers={"HTTP-Referer": "https://repp76.dev", "X-Title": "Codex"},
        )
