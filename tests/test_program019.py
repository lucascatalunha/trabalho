from programs import convert_meters_to_centimeters


def test_01():
    result = convert_meters_to_centimeters(5.5)
    assert result == 550.0


def test_02():
    result = convert_meters_to_centimeters(0.3)
    assert result == 30.0


def test_03():
    result = convert_meters_to_centimeters(10.25)
    assert result == 1025.0


def test_04():
    result = convert_meters_to_centimeters(2)
    assert result == 200
