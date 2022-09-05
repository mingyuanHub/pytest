# content of test_assert2.py
import pytest


def test_set_comparison():
    set1 = set("1308")
    set2 = set("3108")
    assert set1 == set2


if __name__ == "__mian__":
    pytest.main(["-s", "test_set.py"])