import pytest

@pytest.mark.parametrize("num1,num2,output",[(1,2,3),(2,2,4),(3,3,9)])
def test_sum(num1,num2,output):
    assert output == num1+num2