from ordenar.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta([3, 1, 2]) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta([3, 1, 2])) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta([3, 1, 2]) == [1, 2, 3], f"Esperado valor [1, 2, 3]"
    assert resposta(['banana', 'abacaxi', 'manga']) == ['abacaxi', 'banana', 'manga'], f"Esperado valor ['abacaxi', 'banana', 'manga']"

