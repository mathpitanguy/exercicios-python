from salario_descontos.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, 10)) == tuple, "Esperado uma tupla"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(10, 160) == (1600, 176, 128, 80, 1216), f"Esperado valor (1600, 176, 128, 80, 1216)"
    assert resposta(20, 100) == (2000, 220, 160, 100, 1520), f"Esperado valor (2000, 220, 160, 100, 1520)"
