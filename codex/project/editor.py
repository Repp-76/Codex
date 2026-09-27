from pathlib import Path

from .undo import UndoStack


class Editor:
    def __init__(self, project_root: str):
        self.root = Path(project_root).resolve()
        self.undo_stack = UndoStack(self.root)

    def create_file(self, rel_path: str, content: str) -> str:
        target = self._resolve(rel_path)
        if target.exists():
            raise FileExistsError(f"{rel_path} already exists. Use edit instead.")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        self.undo_stack.record("create", rel_path, before=None)
        return rel_path

    def edit_file(self, rel_path: str, new_content: str) -> str:
        target = self._resolve(rel_path)
        before = target.read_text(encoding="utf-8") if target.exists() else None
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(new_content, encoding="utf-8")
        self.undo_stack.record("edit", rel_path, before=before)
        return rel_path

    def delete_file(self, rel_path: str) -> str:
        target = self._resolve(rel_path)
        if not target.exists():
            raise FileNotFoundError(rel_path)
        before = target.read_text(encoding="utf-8")
        target.unlink()
        self.undo_stack.record("delete", rel_path, before=before)
        return rel_path

    def rename_file(self, rel_path: str, new_rel_path: str) -> str:
        target = self._resolve(rel_path)
        new_target = self._resolve(new_rel_path)
        if not target.exists():
            raise FileNotFoundError(rel_path)
        new_target.parent.mkdir(parents=True, exist_ok=True)
        target.rename(new_target)
        self.undo_stack.record("rename", rel_path, before=None, after_path=new_rel_path)
        return new_rel_path

    def undo(self) -> str:
        return self.undo_stack.undo(self.root)

    def _resolve(self, rel_path: str) -> Path:
        path = (self.root / rel_path).resolve()
        if self.root != path and self.root not in path.parents:
            raise ValueError("Path escapes project root.")
        return path
