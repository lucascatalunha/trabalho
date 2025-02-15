from programs import add_even


def test_01():
    result = add_even(6, 7, 8, 9)
    assert result == 14


def test_02():
    result = add_even(10, 11, 12, 13)
    assert result == 22


def test_03():
    result = add_even(14, 15, 16, 17)
    assert result == 30


def test_04():
    result = add_even(1, 2, 3, 4, 5)
    assert result == 6
