from converter_para_inteiro.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta('10') is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta('13')) == int or type(resposta('3.2')) == str, "Esperado um inteiro ou uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta('10') == 10, f"Esperado valor '10'"
    assert resposta('1.2') == 'Valor inválido', f"Esperado valor 'Valor inválido'"
    assert resposta('texto') == 'Valor inválido', f"Esperado valor 'Valor inválido'"
