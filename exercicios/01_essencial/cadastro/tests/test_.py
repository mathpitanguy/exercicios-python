from cadastro.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta("João", 25, 1.75) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta("João", 25, 1.75)) == str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 3, "Assinatura da função deverá receber três parâmetros"


def test_options_resposta():
    assert resposta("João", 25, 1.75) == 'Nome: João | Idade: 25 | Altura: 1.75', f"Esperado valor 'Nome: João | Idade: 25 | Altura: 1.75'"
    assert resposta("Maria", 30, 1.60) == 'Nome: Maria | Idade: 30 | Altura: 1.6', f"Esperado valor 'Nome: Maria | Idade: 30 | Altura: 1.6'"
