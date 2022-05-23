def make_a_dict(a,b):
    operation = a + b 
    return {'a':a, 'b':b, 'result': operation}

def test_make_a_dict():
    my_dict = make_a_dict(2,3)
    expected_dict = {'a':2, 'b':3, 'result': 5 }     
    assert my_dict == expected_dict