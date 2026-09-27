import re
from pathlib import Path

SENSITIVE_FILENAMES = {".env", "id_rsa", "id_ed25519", "credentials.json"}
SENSITIVE_EXTENSIONS = {".pem", ".key", ".pfx", ".p12"}

_SECRET_PATTERNS = [
    re.compile(r"(?i)\b(api[_-]?key|token|secret|password)\b\s*[:=]\s*\S+"),
    re.compile(r"sk-[A-Za-z0-9]{10,}"),          # OpenAI/Anthropic-style keys
    re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{30,}\b"),  # Telegram bot token shape
]


def mask_secret(value: str | None) -> str:
    if not value:
        return "not configured"
    if len(value) <= 4:
        return "*" * len(value)
    return "*" * (len(value) - 4) + value[-4:]


def is_sensitive_path(path) -> bool:
    p = Path(path)
    if p.name in SENSITIVE_FILENAMES:
        return True
    if p.suffix.lower() in SENSITIVE_EXTENSIONS:
        return True
    if "ssh" in p.parts:
        return True
    return False


def redact_secrets(text: str) -> str:
    redacted = text
    for pattern in _SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED]", redacted)
    return redacted
