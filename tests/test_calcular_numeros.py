import allure
from src.calcular_numeros import calcular_promedio

@allure.description("Test calculo promedio")
@allure.feature("Calculo promedio")
@allure.epic("Version inicial")
def test_calcular_promedio():
    numeros = [1, 2, 3, 4, 5, 6]
    resultado = calcular_promedio(numeros)
    assert resultado == 3.5
