from programs import is_number_negative


def test_01():
    result = is_number_negative(0)
    assert result is False


def test_02():
    result = is_number_negative(10)
    assert result is False


def test_03():
    result = is_number_negative(-1000)
    assert result is True


def test_04():
    result = is_number_negative(-5)
    assert result is True
