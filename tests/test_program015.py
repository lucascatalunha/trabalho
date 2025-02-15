from programs import minutes_into_seconds


def test_01():
    result = minutes_into_seconds(10)
    assert result == 600


def test_02():
    result = minutes_into_seconds(15)
    assert result == 900


def test_03():
    result = minutes_into_seconds(30)
    assert result == 1800


def test_04():
    result = minutes_into_seconds(5)
    assert result == 300
