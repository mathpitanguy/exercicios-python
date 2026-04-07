from carro_alugado.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 2) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(0, 2)) == float, "Esperado um  float"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois argumentos"


def test_options_resposta():
    assert resposta(100, 2) == 135.0, f"Esperado valor 10000"
    assert resposta(0, 1) == 60.0, f"Esperado valor 1200"
    assert resposta(0, 0) == 0.0, f"Esperado valor 930"
