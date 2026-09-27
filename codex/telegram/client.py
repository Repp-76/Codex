import requests

TELEGRAM_API = "https://api.telegram.org/bot{token}/{method}"


class TelegramResult:
    def __init__(self, ok: bool, error: str | None = None, response: dict | None = None):
        self.ok = ok
        self.error = error
        self.response = response


class TelegramClient:
    """Thin wrapper around the Telegram Bot API. Every call returns a
    TelegramResult instead of raising, so callers never have to guess
    whether a delivery actually succeeded."""

    def __init__(self, bot_token: str):
        self.token = bot_token

    def send_message(self, chat_id: str, text: str) -> TelegramResult:
        return self._post("sendMessage", {"chat_id": chat_id, "text": text}, timeout=15)

    def send_document(self, chat_id: str, file_path: str, caption: str = "") -> TelegramResult:
        try:
            with open(file_path, "rb") as fh:
                return self._post(
                    "sendDocument",
                    {"chat_id": chat_id, "caption": caption},
                    timeout=60,
                    files={"document": fh},
                )
        except OSError as exc:
            return TelegramResult(False, f"Could not open file: {exc}")

    def _post(self, method: str, data: dict, timeout: int, files: dict | None = None) -> TelegramResult:
        url = TELEGRAM_API.format(token=self.token, method=method)
        try:
            if files:
                resp = requests.post(url, data=data, files=files, timeout=timeout)
            else:
                resp = requests.post(url, json=data, timeout=timeout)
        except requests.exceptions.Timeout:
            return TelegramResult(False, "Request timed out.")
        except requests.exceptions.ConnectionError as exc:
            return TelegramResult(False, f"Network error: {exc}")
        except requests.exceptions.RequestException as exc:
            return TelegramResult(False, str(exc))

        try:
            body = resp.json()
        except ValueError:
            return TelegramResult(False, f"Invalid response ({resp.status_code}).")

        if resp.status_code == 200 and body.get("ok"):
            return TelegramResult(True, response=body.get("result"))

        return TelegramResult(False, self._describe_error(resp.status_code, body))

    @staticmethod
    def _describe_error(status_code: int, body: dict) -> str:
        description = body.get("description", "")
        lowered = description.lower()

        if status_code == 401:
            return "Invalid bot token."
        if status_code == 400 and "chat not found" in lowered:
            return "Invalid user ID, or the user has not started the bot."
        if status_code == 403 and "blocked" in lowered:
            return "The bot was blocked by this user."
        if status_code == 403:
            return "Forbidden: the user has not started the bot."
        if status_code == 429:
            return "Rate limited by Telegram."
        if status_code == 413 or "too large" in lowered:
            return "File is too large for Telegram."
        return description or f"Telegram API error ({status_code})."
