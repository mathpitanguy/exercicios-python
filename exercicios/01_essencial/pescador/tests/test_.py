from pescador.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13)) == tuple, "Esperado uma tupla"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(10) == (0, 0), f"Esperado valor (0, 0)"
    assert resposta(70) == (20, 80), f"Esperado valor (20, 80)"
    assert resposta(0) == (0, 0), f"Esperado valor (0, 0)"
