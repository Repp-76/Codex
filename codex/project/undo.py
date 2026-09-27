import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Operation:
    kind: str  # create, edit, delete, rename
    path: str
    before: str | None
    after_path: str | None
    timestamp: float


class UndoStack:
    def __init__(self, project_root: Path):
        self.backup_dir = Path(project_root) / ".codex_backups"
        self.backup_dir.mkdir(exist_ok=True)
        self._stack: list[Operation] = []

    def record(self, kind: str, path: str, before: str | None, after_path: str | None = None):
        self._stack.append(Operation(kind, path, before, after_path, time.time()))

    def can_undo(self) -> bool:
        return bool(self._stack)

    def undo(self, project_root: Path) -> str:
        if not self._stack:
            raise RuntimeError("Nothing to undo.")
        op = self._stack.pop()
        target = Path(project_root) / op.path

        if op.kind == "create":
            if target.exists():
                target.unlink()
            return f"Removed {op.path}"

        if op.kind in ("edit", "delete"):
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(op.before or "", encoding="utf-8")
            return f"Restored {op.path}"

        if op.kind == "rename":
            new_path = Path(project_root) / op.after_path
            if new_path.exists():
                new_path.rename(target)
            return f"Renamed back to {op.path}"

        raise RuntimeError(f"Unknown operation kind: {op.kind}")
