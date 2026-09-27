import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest

from telegram.delivery import TelegramDeliveryManager, MAX_TELEGRAM_FILE_BYTES
from telegram.client import TelegramResult


def _manager(user_id="42"):
    fake_client = Mock()
    fake_client.send_document.return_value = TelegramResult(True, response={"message_id": 1})
    return TelegramDeliveryManager("token", user_id, client=fake_client), fake_client


def test_delivers_normal_file():
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, "app.py")
        f.write_text("print('hi')")
        manager, client = _manager(user_id="u1")

        result = manager.deliver_file(str(f))

        assert result.ok is True
        client.send_document.assert_called_once()


def test_rejects_env_file():
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, ".env")
        f.write_text("OPENAI_API_KEY=sk-secret")
        manager, client = _manager(user_id="u2")

        result = manager.deliver_file(str(f))

        assert result.ok is False
        assert "secret" in result.reason.lower()
        client.send_document.assert_not_called()


def test_rejects_missing_file():
    manager, client = _manager(user_id="u3")
    result = manager.deliver_file("/nonexistent/path/file.py")
    assert result.ok is False
    client.send_document.assert_not_called()


def test_rejects_oversized_file(monkeypatch):
    monkeypatch.setattr("telegram.delivery.MAX_TELEGRAM_FILE_BYTES", 10)
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, "big.py")
        f.write_text("x" * 100)
        manager, client = _manager(user_id="u4")

        result = manager.deliver_file(str(f))

        assert result.ok is False
        assert "size" in result.reason.lower()


def test_duplicate_delivery_is_skipped():
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, "app.py")
        f.write_text("print('hi')")
        manager, client = _manager(user_id="u5")

        first = manager.deliver_file(str(f))
        second = manager.deliver_file(str(f))

        assert first.ok is True
        assert second.ok is True
        client.send_document.assert_called_once()


def test_changed_file_is_resent():
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, "app.py")
        f.write_text("print('hi')")
        manager, client = _manager(user_id="u6")

        manager.deliver_file(str(f))
        f.write_text("print('bye')")
        manager.deliver_file(str(f))

        assert client.send_document.call_count == 2


def test_project_delivery_zips_and_excludes_secrets():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "index.html").write_text("<html></html>")
        Path(tmp, "css").mkdir()
        Path(tmp, "css", "style.css").write_text("body{}")
        Path(tmp, ".env").write_text("SECRET=1")
        manager, client = _manager(user_id="u7")

        result = manager.deliver_project(tmp, ["index.html", "css/style.css", ".env"], "my-project")

        assert result.ok is True
        client.send_document.assert_called_once()
        zip_path = Path(result.path)
        assert zip_path.exists()
        import zipfile
        with zipfile.ZipFile(zip_path) as zf:
            names = zf.namelist()
        assert "index.html" in names
        assert "css/style.css" in names
        assert ".env" not in names


def test_project_delivery_rejects_when_everything_excluded():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, ".env").write_text("SECRET=1")
        manager, client = _manager(user_id="u8")

        result = manager.deliver_project(tmp, [".env"], "my-project")

        assert result.ok is False
        client.send_document.assert_not_called()


def test_delivery_failure_reported_cleanly():
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp, "app.py")
        f.write_text("print('hi')")
        manager, client = _manager(user_id="u9")
        client.send_document.return_value = TelegramResult(False, "Forbidden: the user has not started the bot.")

        result = manager.deliver_file(str(f))

        assert result.ok is False
        assert "started the bot" in result.reason
