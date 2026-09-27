from .base import ProviderError
from .openai_provider import OpenAIProvider
from .gemini_provider import GeminiProvider
from .anthropic_provider import AnthropicProvider
from .deepseek_provider import DeepSeekProvider
from .openrouter_provider import OpenRouterProvider

PROVIDERS = {
    "openai": OpenAIProvider,
    "gemini": GeminiProvider,
    "anthropic": AnthropicProvider,
    "deepseek": DeepSeekProvider,
    "openrouter": OpenRouterProvider,
}


def create_provider(name: str, api_key: str):
    cls = PROVIDERS.get(name)
    if cls is None:
        raise ProviderError(f"Unknown provider: {name}", name, "unknown_provider")
    if not api_key:
        raise ProviderError(f"{name} is not configured. Set its API key in .env.", name, "not_configured")
    return cls(api_key)
