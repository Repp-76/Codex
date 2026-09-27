import time

from providers.base import ProviderError

MAX_RETRIES = 2
BACKOFF_BASE = 1.5


class Engine:
    def __init__(self, provider_factory, config):
        self.provider_factory = provider_factory
        self.config = config

    def ask(self, provider_name, api_key, messages, model, temperature, max_tokens, fallback=None):
        provider = self.provider_factory(provider_name, api_key)
        try:
            return self._call_with_retry(provider, messages, model, temperature, max_tokens)
        except ProviderError:
            if fallback:
                fb_name, fb_key = fallback
                fallback_provider = self.provider_factory(fb_name, fb_key)
                return self._call_with_retry(fallback_provider, messages, model, temperature, max_tokens)
            raise

    def _call_with_retry(self, provider, messages, model, temperature, max_tokens):
        last_error = None
        for attempt in range(MAX_RETRIES + 1):
            try:
                temp = temperature if provider.supports_temperature else None
                return provider.chat(messages, model, temp, max_tokens)
            except ProviderError as exc:
                last_error = exc
                if not exc.retryable or attempt == MAX_RETRIES:
                    raise
                time.sleep(BACKOFF_BASE ** attempt)
        raise last_error
