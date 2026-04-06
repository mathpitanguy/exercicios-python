def resposta(n):
    n = int(n)

    contador = 0
    lista = list(range(n))

    for item in lista:
         if item % 3 == 0 or item % 5 == 0:
            contador = contador + item

    return contador
