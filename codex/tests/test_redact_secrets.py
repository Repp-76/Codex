from utils.security import redact_secrets


def test_redacts_key_value_pairs():
    text = "here is my config\nOPENAI_API_KEY=sk-abcdefghijklmnop\nDONE"
    redacted = redact_secrets(text)
    assert "sk-abcdefghijklmnop" not in redacted
    assert "[REDACTED]" in redacted


def test_redacts_telegram_bot_token_shape():
    text = "token: 123456789:AAExampleTelegramBotTokenValue1234"
    redacted = redact_secrets(text)
    assert "AAExampleTelegramBotTokenValue1234" not in redacted


def test_leaves_normal_text_alone():
    text = "This function reads a config file and prints hello world."
    assert redact_secrets(text) == text
