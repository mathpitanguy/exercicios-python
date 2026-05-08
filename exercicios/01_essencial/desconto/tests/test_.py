from desconto.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, 10)) == tuple, "Esperado uma tupla"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(100, 10) == (10, 90), f"Esperado valor (10, 90)"
    assert resposta(200, 25) == (50, 150), f"Esperado valor (50, 150)"
    assert resposta(100, 0) == (0, 100), f"Esperado valor (0, 100)"
