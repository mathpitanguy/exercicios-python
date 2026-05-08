from quantidade_preco.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13)) == tuple, "Esperado uma tupla"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(10) == (1, 80.0), f"Esperado valor (1, 80.0)"
    assert resposta(60) == (2, 160), f"Esperado valor (2, 160)"
