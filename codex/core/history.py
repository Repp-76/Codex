from providers.base import ChatMessage

MAX_HISTORY_CHARS = 12000


class History:
    def __init__(self):
        self._messages: list[ChatMessage] = []

    def add(self, role: str, content: str):
        self._messages.append(ChatMessage(role=role, content=content))
        self._trim()

    def _trim(self):
        total = sum(len(m.content) for m in self._messages)
        while total > MAX_HISTORY_CHARS and len(self._messages) > 2:
            removed = self._messages.pop(0)
            total -= len(removed.content)

    def as_list(self) -> list[ChatMessage]:
        return list(self._messages)

    def clear(self):
        self._messages.clear()
