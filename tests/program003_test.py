from programs import club_entry


def test_01():
    result = club_entry(20)
    assert result is False


def test_02():
    result = club_entry(21)
    assert result is True


def test_03():
    result = club_entry(15)
    assert result is False


def test_04():
    result = club_entry(30)
    assert result is True
