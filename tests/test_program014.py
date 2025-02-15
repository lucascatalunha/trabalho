from programs import add_to_number


def test_01():
    result = add_to_number(18)
    assert result == 28


def test_02():
    result = add_to_number(777)
    assert result == 787


def test_03():
    result = add_to_number(-10)
    assert result == 0


def test_04():
    result = add_to_number(4)
    assert result == 14
