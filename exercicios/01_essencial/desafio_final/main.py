from datetime import datetime

EMAIL = "joaozinho.souza@hotmail.com"
FRASE = "Python mudou a forma como eu trabalho!"

emails = [
    "joao.silva@prefeitura.gov.br",
    "ana.souza@camara.gov.br",
    "carlos.lima@gmail.com",
    "beatriz.costa@estadual.gov.br",
    "pedro.mendes@yahoo.com",
]

concluintes = [
    "JOAO SILVA",
    "ANA SOUZA",
    "BEATRIZ COSTA",
]


def gerar_card(emails: list, email: str, frase: str) -> str:
    # Passo 1: adicionar o e-mail à lista
    emails.append(email)

    # Passo 2: tratar os e-mails
    nomes_tratados = []

    for email_atual in emails:
        nome_tratado = email_atual.split("@")[0]
        nome_tratado = nome_tratado.replace(".", " ")
        nome_tratado = nome_tratado.upper()
        nomes_tratados.append(nome_tratado)

    # Passo 3: pegar o último nome (o e-mail recém-adicionado)
    nome = nomes_tratados[-1]

    # Passo 4: verificar status
    if nome in concluintes:
        status = "Curso TrilhaDev Concluído"
    else:
        status = "Curso TrilhaDev em Andamento"

    # Passo 5: data atual
    data = datetime.now().strftime("%d/%m/%Y")

    # Passo 6: montar o card
    card = (
        f"NOME: {nome}\n"
        f"STATUS: {status}\n"
        f"FRASE: {frase}\n"
        f"DATA DE CONCLUSÃO: {data}"
    )

    return card