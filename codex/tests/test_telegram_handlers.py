from telegram.handlers import wants_file


def test_detects_file_request():
    assert wants_file("send this as a python file please")
    assert wants_file("can you export this?")


def test_normal_question_does_not_trigger_file():
    assert not wants_file("how does async python work?")
