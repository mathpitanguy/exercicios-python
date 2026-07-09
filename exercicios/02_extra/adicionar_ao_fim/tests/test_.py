from adicionar_ao_fim.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta([], 1) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta([], 1)) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta([], 1) == [1], f"Esperado valor [1]"
    assert resposta(['banana', 'laranja'], 'manga') == ['banana', 'laranja', 'manga'], f"Esperado valor ['banana', 'laranja', 'manga']"
