from programs import sum_of_three_numbers


def test_01():
    result = sum_of_three_numbers(5, 6, 7)
    assert result == 18


def test_02():
    result = sum_of_three_numbers(8, 9, 10)
    assert result == 27


def test_03():
    result = sum_of_three_numbers(11, 12, 13)
    assert result == 36


def test_04():
    result = sum_of_three_numbers(2, 3, 4)
    assert result == 9
