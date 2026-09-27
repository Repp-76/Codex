from .base import AIProvider
from .http_utils import openai_style_chat


class OpenAIProvider(AIProvider):
    name = "openai"
    default_model = "gpt-4o-mini"

    def chat(self, messages, model, temperature, max_tokens):
        return openai_style_chat(
            "https://api.openai.com/v1/chat/completions",
            self.api_key, messages, model, temperature, max_tokens,
            self.name, self.default_model,
        )
