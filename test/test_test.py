import pytest

def f():
    raise SystemExit(1)
    
def test_demo_method1():
    x = 1
    y = 2
    assert x+2 == y, "test pass"

def test_demo_method2():
    x = 6
    y = 3
    assert x-1 == y+2, "test failed"

