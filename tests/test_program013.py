from programs import discount_received


def test_01():
    result = discount_received(1000, 800)
    assert result == 200


def test_02():
    result = discount_received(500, 450)
    assert result == 50


def test_03():
    result = discount_received(1200, 1000)
    assert result == 200


def test_04():
    result = discount_received(200, 150)
    assert result == 50
