from .base import AIProvider, ChatResult, ProviderError
from .http_utils import post_json, raise_for_status


class GeminiProvider(AIProvider):
    name = "gemini"
    default_model = "gemini-2.0-flash"

    def chat(self, messages, model, temperature, max_tokens):
        model_name = model or self.default_model
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model_name}:generateContent?key={self.api_key}"
        )

        system_parts = [m.content for m in messages if m.role == "system"]
        contents = []
        for m in messages:
            if m.role == "system":
                continue
            role = "model" if m.role == "assistant" else "user"
            contents.append({"role": role, "parts": [{"text": m.content}]})

        payload = {"contents": contents}
        if system_parts:
            payload["systemInstruction"] = {"parts": [{"text": "\n\n".join(system_parts)}]}

        gen_config = {}
        if temperature is not None:
            gen_config["temperature"] = temperature
        if max_tokens:
            gen_config["maxOutputTokens"] = max_tokens
        if gen_config:
            payload["generationConfig"] = gen_config

        resp = post_json(url, {"Content-Type": "application/json"}, payload, self.name)
        if resp.status_code != 200:
            raise_for_status(resp, self.name)

        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            raise ProviderError("Gemini returned no candidates.", self.name, "empty_response", retryable=False)

        text = "".join(part.get("text", "") for part in candidates[0]["content"]["parts"])
        return ChatResult(text=text, model=model_name, provider=self.name, usage=data.get("usageMetadata", {}))
