from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class ChatMessage:
    role: str
    content: str


@dataclass
class ChatResult:
    text: str
    model: str
    provider: str
    usage: dict = field(default_factory=dict)


class ProviderError(Exception):
    def __init__(self, message: str, provider: str, code: str = "unknown", retryable: bool = False):
        super().__init__(message)
        self.message = message
        self.provider = provider
        self.code = code
        self.retryable = retryable


class AIProvider(ABC):
    name: str = "base"
    supports_temperature: bool = True
    supports_streaming: bool = False
    default_model: str = ""

    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def chat(self, messages: list[ChatMessage], model: str, temperature: float | None, max_tokens: int | None) -> ChatResult:
        ...
