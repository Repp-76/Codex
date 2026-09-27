from core.patch import extract_code_blocks, guess_filename


def test_extracts_plain_code_block():
    text = "Sure, here you go:\n```python\nprint('hi')\n```\n"
    blocks = extract_code_blocks(text)
    assert blocks == [("python", "print('hi')")]


def test_guess_filename_uses_language_extension():
    assert guess_filename("python", 0) == "codex_output.py"
    assert guess_filename("html", 0) == "codex_output.html"
    assert guess_filename("unknownlang", 0) == "codex_output.txt"


def test_guess_filename_suffixes_subsequent_blocks():
    assert guess_filename("python", 0) == "codex_output.py"
    assert guess_filename("python", 1) == "codex_output_2.py"
