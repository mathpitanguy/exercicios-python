from _divisao_03_e_05.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(13)) == int, "Esperado um inteiro"
    assert type(resposta(15)) == str, "Esperado uma string"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"

def test_options_resposta():
    assert resposta(3) == 'Fizz' , f"Esperado valor 'Fizz'"
    assert resposta(5) == 'Buzz' , f"Esperado valor 'Buzz'"
    assert resposta(15) == 'FizzBuzz' , f"Esperado valor 'FizzBuzz'"
    assert resposta(2) == 2, f" Esperando 2"