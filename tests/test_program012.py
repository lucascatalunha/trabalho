from programs import square_number


def test_01():
    result = square_number(3)
    assert result == 9


def test_02():
    result = square_number(10)
    assert result == 100


def test_03():
    result = square_number(12)
    assert result == 144


def test_04():
    result = square_number(5)
    assert result == 25
