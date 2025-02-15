from programs import is_number_even


def test_01():
    result = is_number_even(0)
    assert result is True


def test_02():
    result = is_number_even(3)
    assert result is False


def test_03():
    result = is_number_even(-6)
    assert result is True


def test_04():
    result = is_number_even(4)
    assert result is True
