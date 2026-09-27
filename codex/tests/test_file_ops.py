import tempfile
from pathlib import Path

from project.manager import Project
from project.editor import Editor


def test_create_and_read_file():
    with tempfile.TemporaryDirectory() as tmp:
        editor = Editor(tmp)
        editor.create_file("app.py", "print('hi')\n")

        project = Project(tmp)
        assert "app.py" in project.list_files()
        assert project.read_file("app.py") == "print('hi')\n"


def test_ignores_sensitive_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, ".env").write_text("SECRET=1")
        project = Project(tmp)
        assert ".env" not in project.list_files()
        assert project.read_file(".env") is None


def test_path_cannot_escape_root():
    with tempfile.TemporaryDirectory() as tmp:
        editor = Editor(tmp)
        try:
            editor.create_file("../outside.py", "x = 1")
            assert False, "expected ValueError"
        except ValueError:
            pass
