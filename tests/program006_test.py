from programs import hours_into_minutes


def test_01():
    result = hours_into_minutes(1)
    assert result == 60


def test_02():
    result = hours_into_minutes(3)
    assert result == 180


def test_03():
    result = hours_into_minutes(5)
    assert result == 300


def test_04():
    result = hours_into_minutes(2)
    assert result == 120
