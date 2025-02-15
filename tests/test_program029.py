from programs import dashing_numbers


def test_01():
    result = dashing_numbers(6)
    assert result == "------"


def test_02():
    result = dashing_numbers(2)
    assert result == "--"


def test_03():
    result = dashing_numbers(4)
    assert result == "----"


def test_04():
    result = dashing_numbers(1)
    assert result == "-"
