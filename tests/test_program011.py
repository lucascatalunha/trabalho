from programs import correct_sentence


def test_01():
    result = correct_sentence("hello world")
    assert result == "Hello world."


def test_02():
    result = correct_sentence("python is fun.")
    assert result == "Python is fun."


def test_03():
    result = correct_sentence("i love coding")
    assert result == "I love coding."


def test_04():
    result = correct_sentence("this is a test")
    assert result == "This is a test."
