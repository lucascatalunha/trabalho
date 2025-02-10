from programs import passfail


def test_01():
    result = passfail(49)
    assert result == "Failed"


def test_02():
    result = passfail(50)
    assert result == "Passed"


def test_03():
    result = passfail(70)
    assert result == "Passed"


def test_04():
    result = passfail(60)
    assert result == "Passed"
