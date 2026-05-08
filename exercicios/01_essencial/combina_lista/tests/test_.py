from combina_lista.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta([1, 2], [7, 8]) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta([1, 2], [7, 8])) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta([1, 2], [7, 8]) == [1, 2, 7, 8], f"Esperado valor [1, 2, 8, 9]"
    assert resposta([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6], f"Esperado valor [1, 2, 3, 4, 5, 6])"
