# Pytest

Aprendiendo sobre tests unitarios con Pytest, 
siguiendo la documentación de Pytest -> https://docs.pytest.org/en/7.1.x/getting-started.html#getstarted 
y el video de **PyConAr 2020 - Unit Testing: Qué Testear y cómo Testear con PyTest
Sofía Denner** de https://www.youtube.com/watch?v=E4Yc8dhM638&t=343s

## Fases de un test
* Arrange : Preparación
* Act : Ejecución
* Assert : Validación

## Comando útiles
pytest --help -> nos muestra todos los comandos disponibles
pytest tests/folder/test_file.py::test_name -> para lanzar un test en específico
pytest -m smoke -> marcadores
pytest -k users -> filtros

## Suite: para repetir los tests fallidos
pytest --fail-first
pytest --last-failed
pytest --failed-first
*Dar prioridad a los tests fallidos
Plugin: pytest-xdist -> lanza los tests en paralelo

## Setup
* Parametrization
* Fixtures
* Factories
* Arrange o Preparación

## Marks
@pytest.mark.nombre_x
(le pongo este decorador solo a los test q quiero q se corran)
Para correrlo --> pytest -m nombre_de_la_marca -vvv
Si quiero correr todos menos este --> pytest -m "not nombre_de_la_marca" -vvv

## -k selection
pytest -k palabra_clave -vvv
Va a correr solo los test q en alguna parte del nombre o del modulo tenga la palabra q le paso por parámetro.

## Fixtures
Nos ayuda a escribir tests con buen estilo
Es una función q vamos a ejecutar antes de ejecutar nuestro test
También podemos ejecutar código despues de ejecutar el test
En vez de hacer un return hacemos un yield, todo lo q esté antes del yield se va a ejecutar antes de ejecutar nuestro test
Lo q está despues del yield se va a ejecutar despues de correr el test, aunk este haya pasado o no

## Pytest-mock
Se pueden reutilizar
Una librería de pytest -->  pytest-mock
Se instala x separado --> pip install pytest-mock

## Parametrize
Para probar el test con distintos valores?
Si quiero ejecutar solo este test --> pytest -k param -vvv


