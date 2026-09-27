import tempfile
from pathlib import Path

from project.editor import Editor
from project.manager import Project


def test_undo_restores_edit():
    with tempfile.TemporaryDirectory() as tmp:
        editor = Editor(tmp)
        editor.create_file("a.txt", "one")
        editor.edit_file("a.txt", "two")
        editor.undo()
        assert Project(tmp).read_file("a.txt") == "one"


def test_undo_removes_created_file():
    with tempfile.TemporaryDirectory() as tmp:
        editor = Editor(tmp)
        editor.create_file("b.txt", "content")
        editor.undo()
        assert not (Path(tmp) / "b.txt").exists()
