from programs import can_you_vote


def test_01():
    result = can_you_vote(17)
    assert result is False


def test_02():
    result = can_you_vote(18)
    assert result is True


def test_03():
    result = can_you_vote(21)
    assert result is True


def test_04():
    result = can_you_vote(20)
    assert result is True
