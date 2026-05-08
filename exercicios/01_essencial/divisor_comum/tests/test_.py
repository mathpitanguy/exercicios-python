from divisor_comum.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 5) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10, 5)) == int, "Esperado um inteiro."


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(12, 8) == 4, f"Esperado valor 4"
    assert resposta(15, 5) == 5, f"Esperado valor 5"
    assert resposta(21, 14) == 7, f"Esperado valor 7"

