def resposta(numero1, numero2):

    while numero2 != 0:
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto

    return (numero1)

