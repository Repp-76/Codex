import hashlib
import zipfile
from pathlib import Path

from utils.security import is_sensitive_path
from .client import TelegramClient
from . import formatter

MAX_TELEGRAM_FILE_BYTES = 50 * 1024 * 1024  # Telegram Bot API document limit
IGNORED_PROJECT_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".codex_backups", "dist", "build"}

# Shared across TelegramDeliveryManager instances (keyed by "user_id:path") so a
# file isn't resent every time a new manager is created for a single command.
_DELIVERY_CACHE: dict[str, str] = {}


class DeliveryResult:
    def __init__(self, ok: bool, reason: str | None = None, path: str | None = None):
        self.ok = ok
        self.reason = reason
        self.path = path


class TelegramDeliveryManager:
    """Sends generated files, zipped projects, and conversation exports to the
    configured Telegram user. Every path is verified (exists, regular file,
    not a secret, under the size limit) before it's ever uploaded."""

    def __init__(self, bot_token: str, user_id: str, client: TelegramClient | None = None):
        self.client = client or TelegramClient(bot_token)
        self.user_id = user_id

    def deliver_file(self, path: str) -> DeliveryResult:
        check = self._validate_file(path)
        if not check.ok:
            return check

        if self._already_sent(path):
            return DeliveryResult(True, reason="unchanged since last delivery", path=path)

        result = self.client.send_document(self.user_id, path, formatter.document_caption(path))
        if result.ok:
            self._mark_sent(path)
            return DeliveryResult(True, path=path)
        return DeliveryResult(False, reason=result.error, path=path)

    def deliver_project(self, root: str, files: list[str], project_name: str) -> DeliveryResult:
        safe_files = [f for f in files if not self._is_excluded(f) and not is_sensitive_path(f)]
        if not safe_files:
            return DeliveryResult(False, reason="No files to package.")

        zip_path = Path(root) / f"{project_name}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for rel in safe_files:
                zf.write(Path(root) / rel, arcname=rel)

        check = self._validate_file(str(zip_path))
        if not check.ok:
            return check

        result = self.client.send_document(
            self.user_id, str(zip_path), formatter.zip_caption(project_name, len(safe_files))
        )
        if result.ok:
            self._mark_sent(str(zip_path))
            return DeliveryResult(True, path=str(zip_path))
        return DeliveryResult(False, reason=result.error, path=str(zip_path))

    def deliver_chat_export(self, path: str) -> DeliveryResult:
        check = self._validate_file(path)
        if not check.ok:
            return check

        result = self.client.send_document(self.user_id, path, formatter.chat_export_caption())
        if result.ok:
            self._mark_sent(path)
            return DeliveryResult(True, path=path)
        return DeliveryResult(False, reason=result.error, path=path)

    def _validate_file(self, path: str) -> DeliveryResult:
        p = Path(path)
        if not p.exists():
            return DeliveryResult(False, "File does not exist.", path)
        if not p.is_file():
            return DeliveryResult(False, "Not a regular file; directories must be zipped.", path)
        if is_sensitive_path(p):
            return DeliveryResult(False, "Refused: file looks like a secret (.env, key, credentials).", path)
        try:
            size = p.stat().st_size
        except OSError as exc:
            return DeliveryResult(False, f"Could not read file: {exc}", path)
        if size == 0:
            return DeliveryResult(False, "File is empty.", path)
        if size > MAX_TELEGRAM_FILE_BYTES:
            return DeliveryResult(False, "File exceeds Telegram's size limit.", path)
        return DeliveryResult(True, path=path)

    def _is_excluded(self, rel_path: str) -> bool:
        return any(part in IGNORED_PROJECT_DIRS for part in Path(rel_path).parts)

    def _already_sent(self, path: str) -> bool:
        key = f"{self.user_id}:{path}"
        return _DELIVERY_CACHE.get(key) == self._hash_file(path)

    def _mark_sent(self, path: str):
        key = f"{self.user_id}:{path}"
        _DELIVERY_CACHE[key] = self._hash_file(path)

    @staticmethod
    def _hash_file(path: str) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
