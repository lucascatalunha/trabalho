from programs import area_of_circle


def test_01():
    result = area_of_circle(10)
    assert result == 314.16


def test_02():
    result = area_of_circle(3.5)
    assert result == 38.48


def test_03():
    result = area_of_circle(7.1)
    assert result == 158.37


def test_04():
    result = area_of_circle(5)
    assert result == 78.54
