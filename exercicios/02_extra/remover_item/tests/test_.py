from remover_item.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(['a', 'b', 'a'], 'a') is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(['a', 'b', 'a'], 'a')) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(['a', 'b', 'a'], 'a') == ['b', 'a'], f"Esperado valor ['b', 'a']"
    assert resposta(['x', 'y'], 'z') == ['x', 'y'], f"Esperado valor 1200"
