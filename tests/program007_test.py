from programs import double_number


def test_01():
    result = double_number(3)
    assert result == 6


def test_02():
    result = double_number(0)
    assert result == 0


def test_03():
    result = double_number(-4)
    assert result == -8


def test_04():
    result = double_number(5)
    assert result == 10
