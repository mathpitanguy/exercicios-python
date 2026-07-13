import random

def gerar_mensagem(nome):
    # Passo 1 — gera uma chave aleatória entre 1 e 25
    chave = random.randint(1, 25)

    # Passo 2 — monta a mensagem original (caixa alta, sem acentos)
    mensagem = f"PARABENS, {nome.upper()}! VOCE ESTA VOANDO BAIXO."

    # Passo 3 — codifica a mensagem com a Cifra de César
    mensagem_codificada = ""
    for char in mensagem:
        if char.isalpha():
            novo_indice = (ord(char) - ord('A') + chave) % 26
            nova_letra = chr(novo_indice + ord('A'))
            mensagem_codificada += nova_letra
        else:
            mensagem_codificada += char

    return chave, mensagem_codificada


# Exemplo de uso
chave, mensagem_codificada = gerar_mensagem("MATHEUS") # Insira o nome do aluno(a) aqui.
print(f"Chave: {chave}")
print(f"Mensagem codificada: {mensagem_codificada}")

alfabeto = ""
for i in range(97, 123):  # 97 é o código de 'a', 122 é o código de 'z'
    alfabeto += chr(i)

print(alfabeto)  # "abcdefghijklmnopqrstuvwxyz"
