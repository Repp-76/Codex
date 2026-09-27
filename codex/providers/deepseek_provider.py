from .base import AIProvider
from .http_utils import openai_style_chat


class DeepSeekProvider(AIProvider):
    name = "deepseek"
    default_model = "deepseek-chat"

    def chat(self, messages, model, temperature, max_tokens):
        return openai_style_chat(
            "https://api.deepseek.com/chat/completions",
            self.api_key, messages, model, temperature, max_tokens,
            self.name, self.default_model,
        )
