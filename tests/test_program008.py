from programs import is_number_odd


def test_01():
    result = is_number_odd(4)
    assert result is False


def test_02():
    result = is_number_odd(7)
    assert result is True


def test_03():
    result = is_number_odd(10)
    assert result is False


def test_04():
    result = is_number_odd(3)
    assert result is True
