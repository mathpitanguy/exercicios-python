from triangulo.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 10, 10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, 10, 10)) == str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 3, "Assinatura da função deverá receber três parâmetros"


def test_options_resposta():
    assert resposta(1, 2, 3) == "não forma triângulo", f"Esperado valor 'não forma triângulo'"
    assert resposta(3, 4, 5) == "escaleno", f"Esperado valor 'escaleno'"
    assert resposta(3, 3, 3) == "equilátero", f"Esperado valor 'equilátero'"
    assert resposta(2, 2, 3) == "isósceles", f"Esperando valor 'isósceles'"
