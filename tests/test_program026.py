from programs import convert_to_titlecase


def test_01():
    result = convert_to_titlecase("python programming is fun")
    assert result == "Python Programming Is Fun"


def test_02():
    result = convert_to_titlecase("good morning everyone")
    assert result == "Good Morning Everyone"


def test_03():
    result = convert_to_titlecase("happy coding!")
    assert result == "Happy Coding!"


def test_04():
    result = convert_to_titlecase("hello world")
    assert result == "Hello World"
