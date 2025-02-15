from programs import adding_ends


def test_01():
    result = adding_ends(10, 20, 30)
    assert result == 40


def test_02():
    result = adding_ends(-5, -10)
    assert result == -15


def test_03():
    result = adding_ends(0, 1000)
    assert result == 1000


def test_04():
    result = adding_ends(1, 2, 3, 4, 5)
    assert result == 6
