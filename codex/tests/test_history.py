from core.history import History


def test_trims_when_over_budget():
    history = History()
    for _ in range(50):
        history.add("user", "x" * 1000)
    total = sum(len(m.content) for m in history.as_list())
    assert total <= 12000
    assert len(history.as_list()) >= 2
