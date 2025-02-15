from programs import convert_hours_into_seconds


def test_01():
    result = convert_hours_into_seconds(1)
    assert result == 3600


def test_02():
    result = convert_hours_into_seconds(2)
    assert result == 7200


def test_03():
    result = convert_hours_into_seconds(3)
    assert result == 10800


def test_04():
    result = convert_hours_into_seconds(4)
    assert result == 14400
