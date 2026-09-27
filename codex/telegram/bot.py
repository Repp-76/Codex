import time
import requests

from .sender import TelegramSender


class TelegramBot:
    """Long-polling Telegram bot. Routes incoming text through on_message(text) -> reply."""

    def __init__(self, bot_token: str, on_message):
        self.token = bot_token
        self.sender = TelegramSender(bot_token)
        self.on_message = on_message
        self._offset = 0

    def poll_forever(self):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        while True:
            try:
                resp = requests.get(url, params={"offset": self._offset, "timeout": 30}, timeout=35)
                resp.raise_for_status()
            except requests.exceptions.RequestException:
                time.sleep(5)
                continue

            for update in resp.json().get("result", []):
                self._offset = update["update_id"] + 1
                message = update.get("message")
                if not message or "text" not in message:
                    continue
                chat_id = message["chat"]["id"]
                reply_text = self.on_message(message["text"])
                self.sender.send_message(chat_id, reply_text)
