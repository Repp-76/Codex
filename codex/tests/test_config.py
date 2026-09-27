import importlib


def test_configured_providers(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test1234")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    import config as config_module
    importlib.reload(config_module)

    assert "openai" in config_module.config.configured_providers()
    assert "gemini" not in config_module.config.configured_providers()


def test_mask_secret():
    from utils.security import mask_secret

    assert mask_secret(None) == "not configured"
    assert mask_secret("abcd") == "****"
    masked = mask_secret("sk-1234567890")
    assert masked.endswith("7890")
    assert masked.startswith("*")
