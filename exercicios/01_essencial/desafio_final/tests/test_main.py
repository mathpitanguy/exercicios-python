from cifra_cesar.main import decodificar
import inspect
import pytest


def test_not_none():
    assert decodificar("EBWDJFHI", 4) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(decodificar("EBWDJFHI", 4)) == str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(decodificar).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_decodificacao_com_chave_conhecida():
    # "OLA" codificado com chave 3 vira "ROD"
    assert decodificar("ROD", 3) == "OLA", 'Esperado "OLA" ao decodificar "ROD" com chave 3'


def test_decodificacao_mantem_espacos_e_pontuacao():
    # "PARABENS, ANA!" codificado com chave 5 vira "UFWFGJSX, FSF!"
    codificado = "UFWFGJSX, FSF!"
    assert decodificar(codificado, 5) == "PARABENS, ANA!", "Espaços, vírgula e exclamação devem ser mantidos"


def test_decodificacao_com_chave_grande():
    # Testa o caso em que a subtração dá negativo, validando o uso do % 26
    # "B" codificado com chave 5 vira "G"; decodificar "G" com chave 5 deve voltar a ser "B"
    assert decodificar("G", 5) == "B", "Esperado que a decodificação trate corretamente o caso de índice negativo"


def test_mensagem_final():
    # ==========================================================
    # Substitua os valores abaixo pelos dados enviados na Issue
    # ==========================================================
    nome = "NOME_DA_PESSOA"
    mensagem_codificada = "UFWFGJSX, OTFT! WTHZ HTSHRZNZ T HZANT KJ UDYATS"
    chave = 5
    # ==========================================================

    mensagem_decodificada = decodificar(mensagem_codificada, chave)
    mensagem_esperada = f"PARABENS, {nome.upper()}! VOCE CONCLUIU O CURSO DE PYTHON"

    assert isinstance(mensagem_decodificada, str), "Esperado uma string"
    assert mensagem_decodificada == mensagem_esperada, (
        f"Mensagem decodificada não confere com o padrão esperado. "
        f"Verifique se 'nome', 'mensagem_codificada' e 'chave' foram preenchidos corretamente."
    )

    print(f"\nMensagem decodificada: {mensagem_decodificada}")
