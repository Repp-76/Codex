from unittest.mock import Mock, patch

from telegram.client import TelegramClient


def _resp(status, body):
    m = Mock()
    m.status_code = status
    m.json.return_value = body
    return m


def test_send_message_success():
    client = TelegramClient("token")
    with patch("telegram.client.requests.post", return_value=_resp(200, {"ok": True, "result": {"message_id": 1}})):
        result = client.send_message("123", "hi")
    assert result.ok is True
    assert result.response == {"message_id": 1}


def test_invalid_token():
    client = TelegramClient("bad-token")
    with patch("telegram.client.requests.post", return_value=_resp(401, {"ok": False, "description": "Unauthorized"})):
        result = client.send_message("123", "hi")
    assert result.ok is False
    assert "token" in result.error.lower()


def test_chat_not_found():
    client = TelegramClient("token")
    body = {"ok": False, "description": "Bad Request: chat not found"}
    with patch("telegram.client.requests.post", return_value=_resp(400, body)):
        result = client.send_message("000", "hi")
    assert result.ok is False
    assert "not started the bot" in result.error or "Invalid user ID" in result.error


def test_bot_blocked():
    client = TelegramClient("token")
    body = {"ok": False, "description": "Forbidden: bot was blocked by the user"}
    with patch("telegram.client.requests.post", return_value=_resp(403, body)):
        result = client.send_message("123", "hi")
    assert result.ok is False
    assert "blocked" in result.error.lower()


def test_rate_limited():
    client = TelegramClient("token")
    with patch("telegram.client.requests.post", return_value=_resp(429, {"ok": False, "description": "Too Many Requests"})):
        result = client.send_message("123", "hi")
    assert result.ok is False
    assert "rate limited" in result.error.lower()


def test_timeout():
    import requests
    client = TelegramClient("token")
    with patch("telegram.client.requests.post", side_effect=requests.exceptions.Timeout()):
        result = client.send_message("123", "hi")
    assert result.ok is False
    assert "timed out" in result.error.lower()


def test_connection_error():
    import requests
    client = TelegramClient("token")
    with patch("telegram.client.requests.post", side_effect=requests.exceptions.ConnectionError("dns fail")):
        result = client.send_message("123", "hi")
    assert result.ok is False
    assert "network error" in result.error.lower()
