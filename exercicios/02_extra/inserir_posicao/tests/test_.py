from inserir_posicao.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(['banana', 'manga'], 1, 'laranja') is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(['banana', 'manga'], 1, 'laranja')) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 3, "Assinatura da função deverá receber três parâmetros"


def test_options_resposta():
    assert resposta(['banana', 'manga'], 1, 'laranja') == ['banana', 'laranja', 'manga'], f"Esperado valor ['banana', 'laranja', 'manga']"
    assert resposta(['b', 'c'], 0, 'a') == ['a', 'b', 'c'], f"Esperado valor ['a', 'b', 'c']"
