from maior_menor.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 20, 30) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13, 14, 15)) == tuple, "Esperado uma tupla"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 3, "Assinatura da função deverá receber três parâmetros"

def test_options_resposta():
    assert resposta(10, 20, 5) == (20, 5), f"Esperado valor (20, 5)"
    assert resposta(7, 3, 9) == (9, 3), f"Esperado valor (9, 3)"
    assert resposta(4, 4, 2) == (4, 2), f"Esperado valor (4, 2)"
