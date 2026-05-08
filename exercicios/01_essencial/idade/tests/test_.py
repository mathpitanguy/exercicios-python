from idade.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta('1996') is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta('1986')) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta('2000') == 26, f"Esperado valor 26"
    assert resposta('2026') == 0, f"Esperado valor 0"
    assert resposta('1926') == 100, f"Esperado valor 100"
