import importlib


def test_user_id_migrates_from_chat_id(monkeypatch):
    monkeypatch.delenv("TELEGRAM_USER_ID", raising=False)
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "999999")

    import config as config_module
    importlib.reload(config_module)

    assert config_module.config.telegram.user_id == "999999"


def test_user_id_takes_priority_over_chat_id(monkeypatch):
    monkeypatch.setenv("TELEGRAM_USER_ID", "111111")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "999999")

    import config as config_module
    importlib.reload(config_module)

    assert config_module.config.telegram.user_id == "111111"


def test_auto_send_defaults(monkeypatch):
    monkeypatch.delenv("TELEGRAM_AUTO_SEND_FILES", raising=False)
    monkeypatch.delenv("TELEGRAM_AUTO_SEND_PROJECTS", raising=False)
    monkeypatch.delenv("TELEGRAM_AUTO_SEND_CHAT", raising=False)

    import config as config_module
    importlib.reload(config_module)

    assert config_module.config.telegram.auto_send_files is True
    assert config_module.config.telegram.auto_send_projects is True
    assert config_module.config.telegram.auto_send_chat is False


def test_auto_send_chat_can_be_enabled(monkeypatch):
    monkeypatch.setenv("TELEGRAM_AUTO_SEND_CHAT", "true")

    import config as config_module
    importlib.reload(config_module)

    assert config_module.config.telegram.auto_send_chat is True
