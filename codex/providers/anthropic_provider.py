from .base import AIProvider, ChatResult
from .http_utils import post_json, raise_for_status


class AnthropicProvider(AIProvider):
    name = "anthropic"
    default_model = "claude-sonnet-4-6"

    def chat(self, messages, model, temperature, max_tokens):
        system_parts = [m.content for m in messages if m.role == "system"]
        convo = [{"role": m.role, "content": m.content} for m in messages if m.role != "system"]

        payload = {
            "model": model or self.default_model,
            "max_tokens": max_tokens or 1024,
            "messages": convo,
        }
        if system_parts:
            payload["system"] = "\n\n".join(system_parts)
        if temperature is not None:
            payload["temperature"] = temperature

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }
        resp = post_json("https://api.anthropic.com/v1/messages", headers, payload, self.name)
        if resp.status_code != 200:
            raise_for_status(resp, self.name)

        data = resp.json()
        text = "".join(block.get("text", "") for block in data.get("content", []) if block.get("type") == "text")
        return ChatResult(text=text, model=payload["model"], provider=self.name, usage=data.get("usage", {}))
