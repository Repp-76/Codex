import json
from pathlib import Path

from constants import STATE_DIR_NAME, STATE_FILE_NAME


def _state_path() -> Path:
    d = Path.home() / STATE_DIR_NAME
    d.mkdir(exist_ok=True)
    return d / STATE_FILE_NAME


def load_state() -> dict:
    path = _state_path()
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(data: dict):
    _state_path().write_text(json.dumps(data, indent=2), encoding="utf-8")
