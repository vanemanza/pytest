import pytest

class Person():
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

def years_until_retirement(persona):        
    edad = persona.age
    return 65 - edad

def name_and_age(persona):      
    nombre = persona.name
    edad = persona.age
    return (nombre, edad)

@pytest.fixture
def person():
    return Person(
        name='foo',
        age = 30,
        profession = 'accountant',
    )

def test_year_until_retirement(person):
    assert years_until_retirement(person) == 35

def test_name_and_age(person):
    assert name_and_age(person) == ("foo", 30)        