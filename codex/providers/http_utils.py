import requests

from .base import ChatResult, ProviderError


def post_json(url, headers, payload, provider_name, timeout=60):
    try:
        return requests.post(url, headers=headers, json=payload, timeout=timeout)
    except requests.exceptions.Timeout:
        raise ProviderError(f"Request to {provider_name} timed out.", provider_name, "timeout", retryable=True)
    except requests.exceptions.ConnectionError as exc:
        raise ProviderError(f"Could not reach {provider_name}: {exc}", provider_name, "connection", retryable=True)


def raise_for_status(resp, provider_name):
    try:
        body = resp.json()
        message = body.get("error", {}).get("message") if isinstance(body.get("error"), dict) else None
        message = message or body.get("message") or resp.text
    except ValueError:
        message = resp.text

    if resp.status_code in (401, 403):
        raise ProviderError("Authentication failed. Check the API key.", provider_name, "auth", retryable=False)
    if resp.status_code == 429:
        raise ProviderError("Rate limit reached. Try again shortly.", provider_name, "rate_limit", retryable=True)
    if resp.status_code == 404:
        raise ProviderError(f"Model not found: {message}", provider_name, "model_not_found", retryable=False)
    if resp.status_code >= 500:
        raise ProviderError(f"Provider outage ({resp.status_code}).", provider_name, "server_error", retryable=True)
    raise ProviderError(str(message), provider_name, "invalid_request", retryable=False)


def openai_style_chat(url, api_key, messages, model, temperature, max_tokens, provider_name, default_model, extra_headers=None):
    payload = {
        "model": model or default_model,
        "messages": [{"role": m.role, "content": m.content} for m in messages],
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if max_tokens:
        payload["max_tokens"] = max_tokens

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)

    resp = post_json(url, headers, payload, provider_name)
    if resp.status_code != 200:
        raise_for_status(resp, provider_name)

    data = resp.json()
    text = data["choices"][0]["message"]["content"]
    return ChatResult(text=text, model=payload["model"], provider=provider_name, usage=data.get("usage", {}))
