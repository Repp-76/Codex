import pytest

from providers.factory import create_provider
from providers.base import ProviderError
from providers.openai_provider import OpenAIProvider


def test_creates_known_provider():
    provider = create_provider("openai", "sk-test")
    assert isinstance(provider, OpenAIProvider)


def test_rejects_unknown_provider():
    with pytest.raises(ProviderError):
        create_provider("madeup", "key")


def test_rejects_missing_key():
    with pytest.raises(ProviderError):
        create_provider("openai", "")
