from programs import free_throw_probability


def test_01():
    result = free_throw_probability(3, 6)
    assert result == 0.5


def test_02():
    result = free_throw_probability(7, 14)
    assert result == 0.5


def test_03():
    result = free_throw_probability(4, 8)
    assert result == 0.5


def test_04():
    result = free_throw_probability(5, 10)
    assert result == 0.5
