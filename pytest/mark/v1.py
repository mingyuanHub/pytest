import pytest

@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [2, 3, 4])
def test_data(a, b):
    print(a, b)