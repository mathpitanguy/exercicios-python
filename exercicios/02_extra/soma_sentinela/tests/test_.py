from soma_sentinela.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta([1, 2, 3]) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta([1, 2, 3])) == int, "Esperado um inteiro."


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta([1, 2, 3]) == 6, f"Esperado valor 6"
    assert resposta([0, 5]) == 0, f"Esperado valor 0"
    assert resposta([4, 7, 2, 0, 9]) == 13, f"Esperado valor 13"
