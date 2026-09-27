from pathlib import Path

from utils.security import is_sensitive_path

IGNORED_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".codex_backups", "dist", "build"}
MAX_FILE_BYTES = 200_000


class Project:
    def __init__(self, root: str):
        self.root = Path(root).resolve()
        if not self.root.exists():
            raise FileNotFoundError(f"Project path does not exist: {self.root}")

    def list_files(self) -> list[str]:
        result = []
        for path in self.root.rglob("*"):
            if path.is_dir():
                continue
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
            if is_sensitive_path(path):
                continue
            result.append(str(path.relative_to(self.root)))
        return sorted(result)

    def read_file(self, rel_path: str) -> str | None:
        try:
            path = self._resolve(rel_path)
        except ValueError:
            return None
        if is_sensitive_path(path) or not path.exists():
            return None
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return None

    def _resolve(self, rel_path: str) -> Path:
        path = (self.root / rel_path).resolve()
        if self.root != path and self.root not in path.parents:
            raise ValueError("Path escapes project root.")
        return path
