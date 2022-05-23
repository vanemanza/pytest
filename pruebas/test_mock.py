import pytest

# instalar mock -> python -m pip install pytest-mock

# mocker es un wraper? de mock, del test de python
# ver la documentacion de unittest de python
def some_calculation(a, b):
    return a + b

def make_a_dict(a,b):
    operation = some_calculation(a,b)
    return {'a':a, 'b':b, 'result':operation}

def test_some_calculation():
    assert some_calculation(1,2) == 3

# para testear make_a_dict sin ejecutar la lógica de some_calculation tenemos q mockear esa funcion
def test_make_a_dict(mocker):
    mocker.patch(
        "test_mock.some_calculation", #lugar donde se importa y se usa la funcion (no! donde se define)
        # donde se está usando la funcion. el nombre de la funcion q vamos a mockear
        return_value = 5, # el valor q queremos q devuelva
        autospect = True, # autoespectro sirve para validar la interfaz
    )    
    my_dict = make_a_dict(2,3)
    expected_dict = {'a':2, 'b':3, 'result':5}
    assert my_dict == expected_dict