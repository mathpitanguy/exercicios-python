from temperatura.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, "C") is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, "C")) == int or type(resposta(10, "C")) == float, "Esperado um inteiro ou float"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(0, "C") == 32.0, f"Esperado valor 32.0"
    assert resposta(32, "F") == 0.0, f"Esperado valor 0.0"
    assert resposta(100, "C") == 212.0, f"Esperado valor 212.0"
