import time

from .client import TelegramClient


class TelegramSender:
    """Backward-compatible thin facade over TelegramClient, used by the
    long-polling bot loop for plain text replies."""

    def __init__(self, bot_token: str):
        self.client = TelegramClient(bot_token)

    def send_message(self, chat_id: str, text: str) -> bool:
        return self.client.send_message(chat_id, text).ok

    def send_document(self, chat_id: str, file_path: str, caption: str = "") -> bool:
        return self.client.send_document(chat_id, file_path, caption).ok


def notify_super_admin(bot_token: str, super_admin_id: str, telegram_id: str) -> bool:
    sender = TelegramSender(bot_token)
    text = (
        "[CODEX] New user configuration\n\n"
        f"Telegram ID: {telegram_id}\n"
        "Status: Configured\n"
        f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    )
    return sender.send_message(super_admin_id, text)
