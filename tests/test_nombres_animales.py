import allure
from src.animales import obtener_nombres_animaes

@allure.description("Test lista nombre animales")
@allure.feature("Lista nombre animales")
@allure.epic("Version inicial")
def test_obtener_nombres_animales():
    nombres = obtener_nombres_animaes()
    assert isinstance(nombres, list)
