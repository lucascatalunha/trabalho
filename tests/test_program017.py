from programs import smallest_of_two_numbers


def test_01():
    result = smallest_of_two_numbers(12, 15)
    assert result == 12


def test_02():
    result = smallest_of_two_numbers(-5, -7)
    assert result == -7


def test_03():
    result = smallest_of_two_numbers(0, 0)
    assert result == 0


def test_04():
    result = smallest_of_two_numbers(8, 3)
    assert result == 3
