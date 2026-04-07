from fumante.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, 10)) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(10, 1) == 25, f"Esperado valor 25"
    assert resposta(10, 10) == 253, f"Esperado valor 253"
