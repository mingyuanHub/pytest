import pytest


@pytest.mark.parametrize('p1', ['1', '2', '3'])
def test_01(cmdopt, p1):
    print(p1)


def test_v1(cmdopt):
    print(cmdopt)
