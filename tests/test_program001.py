from programs import is_number_multiple_of_ten


def test_01():
    result = is_number_multiple_of_ten(100)
    assert result is True


def test_02():
    result = is_number_multiple_of_ten(55)
    assert result is False


def test_03():
    result = is_number_multiple_of_ten(0)
    assert result is True


def test_04():
    result = is_number_multiple_of_ten(30)
    assert result is True
