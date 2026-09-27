from core.patch import parse_file_blocks


def test_parses_single_file_block():
    text = "FILE: app.py\n```python\nprint('hi')\n```\n"
    blocks = parse_file_blocks(text)
    assert blocks == [("app.py", "print('hi')")]


def test_parses_multiple_file_blocks():
    text = (
        "FILE: a.py\n```python\nx = 1\n```\n\n"
        "FILE: b.py\n```python\ny = 2\n```\n"
    )
    blocks = parse_file_blocks(text)
    assert [b[0] for b in blocks] == ["a.py", "b.py"]
