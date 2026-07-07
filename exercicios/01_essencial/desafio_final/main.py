
mensagem = "FQHQRUDI, TEKWBQI! LESU SEDSBKYK E SKHIE TU FOJXED"
chave    = 16
resultado = ""

for char in mensagem:
    if char.isupper():
        resultado += chr((ord(char) - ord('A') - chave) % 26 + ord('A'))
    elif char.islower():
        resultado += chr((ord(char) - ord('a') - chave) % 26 + ord('a'))
    else:
        resultado += char

print(resultado)
