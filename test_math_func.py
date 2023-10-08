import sys
sys.path.append('D:\\python\\')

from math_func import add, product

def test_add():
    assert add(7, 3) == 10
    assert add(7) == 9
    assert add(5) == 7

def test_product():
    assert product(5, 5) == 25
    assert product(5) == 10
    assert product(7) == 14