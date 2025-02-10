from program002 import divisible_by_five


def test_01():
    result = divisible_by_five(15)
    assert result is True


def test_02():
    result = divisible_by_five(17)
    assert result is False


def test_03():
    result = divisible_by_five(25)
    assert result is True


def test_04():
    result = divisible_by_five(10)
    assert result is True
