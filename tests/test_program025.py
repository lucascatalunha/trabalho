from programs import greater_than_five


def test_01():
    result = greater_than_five(3)
    assert result is False


def test_02():
    result = greater_than_five(6)
    assert result is True


def test_03():
    result = greater_than_five(5)
    assert result is False


def test_04():
    result = greater_than_five(7)
    assert result is True
