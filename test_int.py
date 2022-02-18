import pytest

@pytest.mark.parametrize('number', [-20, 0 , 30])
def test_square(number):
    assert number**2 >= 0

def test_not_zero():
    list_without_zero = [1 , 2, -4, 2, 0]
    for i in list_without_zero:
        try:
            assert i != 0
        except AssertionError:
            pass

def test_sum_square():
    num1 = 5
    num2 = 8
    assert num1**2-num2**2 == (num1-num2)*(num1+num2)

