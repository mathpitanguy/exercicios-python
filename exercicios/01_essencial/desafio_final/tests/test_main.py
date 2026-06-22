from desafio_final.main import gerar_card, EMAIL, FRASE, emails, concluintes
import inspect
import pytest
import re


def test_not_none():
    assert gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!") is not None, \
        "Esperado valor diferente de 'None'"


def test_type():
    assert type(gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")) == str, \
        "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(gerar_card).args) == 3, \
        "Assinatura da função deverá receber três parâmetros: emails, email, frase"


def test_email_adicionado():
    lista = emails.copy()
    gerar_card(lista, "novo@email.com", "Frase de teste aqui!")
    assert "novo@email.com" in lista, \
        "O e-mail deve ser adicionado à lista com .append()"


def test_nome_caixa_alta():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "JOAO SILVA" in resultado, \
        "Esperado nome 'JOAO SILVA' em caixa alta e sem ponto"


def test_nome_sem_ponto():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "JOAO.SILVA" not in resultado, \
        "O nome não deve conter '.', substitua por espaço"


def test_nome_sem_arroba():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "@" not in resultado, \
        "O card não deve conter '@', corte o e-mail antes do '@'"


def test_status_concluinte():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "Curso TrilhaDev Concluído" in resultado, \
        "Esperado status 'Curso TrilhaDev Concluído' para JOAO SILVA"


def test_status_em_andamento():
    resultado = gerar_card(emails.copy(), "carlos.lima@gmail.com", "Frase de teste aqui!")
    assert "Curso TrilhaDev em Andamento" in resultado, \
        "Esperado status 'Curso TrilhaDev em Andamento' para CARLOS LIMA"


def test_card_campos():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "NOME:" in resultado, "Esperado campo 'NOME:' no card"
    assert "STATUS:" in resultado, "Esperado campo 'STATUS:' no card"
    assert "FRASE:" in resultado, "Esperado campo 'FRASE:' no card"
    assert "DATA DE CONCLUSÃO:" in resultado, "Esperado campo 'DATA DE CONCLUSÃO:' no card"


def test_card_frase():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert "Frase de teste aqui!" in resultado, \
        "Esperado a frase informada no card"


def test_card_data_formato():
    resultado = gerar_card(emails.copy(), "joao.silva@prefeitura.gov.br", "Frase de teste aqui!")
    assert re.search(r"\d{2}/\d{2}/\d{4}", resultado), \
        "Esperado data no formato DD/MM/AAAA gerada com datetime"


def test_email_preenchido():
    assert EMAIL.strip() != "", \
        "Preencha a variável EMAIL com seu e-mail"


def test_frase_preenchida():
    assert FRASE.strip() != "", \
        "Preencha a variável FRASE com uma frase sobre o curso"


def test_card_final():
    resultado = gerar_card(emails.copy(), EMAIL, FRASE)

    print("\n")
    print("=" * 60)
    print("🏆 SEU CARD — Cole nos comentários do curso!")
    print("=" * 60)
    print(resultado)
    print("=" * 60)

    assert True