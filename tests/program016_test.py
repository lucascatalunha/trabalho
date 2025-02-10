from programs import string_concatenation


def test_01():
    result = string_concatenation("Good", "Morning")
    assert result == "GoodMorning"


def test_02():
    result = string_concatenation("Happy", "Day")
    assert result == "HappyDay"


def test_03():
    result = string_concatenation("Python", "Programming")
    assert result == "PythonProgramming"


def test_04():
    result = string_concatenation("Hello", "World")
    assert result == "HelloWorld"
