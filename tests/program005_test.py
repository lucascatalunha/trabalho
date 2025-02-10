from programs import largest_of_two


def test_01():
    result = largest_of_two(10, 20)
    assert result == 20


def test_02():
    result = largest_of_two(5, 3)
    assert result == 5


def test_03():
    result = largest_of_two(14, 14)
    assert result == 14


def test_04():
    result = largest_of_two(12, 8)
    assert result == 12
