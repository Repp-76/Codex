from ui import banner


class _FakeTelegram:
    enabled = False
    user_id = None
    super_admin_id = None


class _FakeConfig:
    telegram = _FakeTelegram()

    def status_lines(self):
        return [("openai", True, "****abcd")]

    def configured_providers(self):
        return ["openai"]


def test_clear_screen_happens_before_any_output(monkeypatch):
    calls = []
    monkeypatch.setattr(banner, "clear_screen", lambda: calls.append("clear"))
    monkeypatch.setattr(banner.console, "print", lambda *a, **k: calls.append("print"))

    banner.show_startup(_FakeConfig())

    assert calls[0] == "clear"
    assert "print" in calls


def test_clear_screen_uses_ansi_and_os_clear(monkeypatch):
    written = []
    monkeypatch.setattr("ui.banner.os.system", lambda cmd: written.append(("os", cmd)))
    monkeypatch.setattr("ui.banner.sys.stdout.write", lambda s: written.append(("ansi", s)))
    monkeypatch.setattr("ui.banner.sys.stdout.flush", lambda: written.append(("flush", None)))

    banner.clear_screen()

    kinds = [k for k, _ in written]
    assert "os" in kinds
    assert "ansi" in kinds
    assert "flush" in kinds
