import pytest

def some_calculation(a,b):
    return a + b

@pytest.mark.parametrize("a,b,expected_result", [ 
    (1,2,3),
    (3,3,6),
    (3,-2,1),
]) 
def test_some_calculation_param(a,b, expected_result):
    assert some_calculation(a,b) == expected_result   