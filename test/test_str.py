import pytest

@pytest.mark.parametrize(("arg", "expect"), [
    ('', ''),
    (0, '0'),
    (0L, '0'),
    ((), '()'),
    ([], '[]'),
    ({}, '{}'),
])
def test_basic_creation(arg, expect):
    assert str(arg) == expect

