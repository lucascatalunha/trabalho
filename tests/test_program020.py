from programs import odd_even


def test_01():
    result = odd_even(3)
    assert result == "Odd"


def test_02():
    result = odd_even(0)
    assert result == "Even"


def test_03():
    result = odd_even(-5)
    assert result == "Odd"


def test_04():
    result = odd_even(4)
    assert result == "Even"
