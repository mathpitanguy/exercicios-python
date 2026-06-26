def resposta(n):
    fibonacci = [1,1]
    while len(fibonacci) < n:
        resultado = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(resultado)
    return (fibonacci[-1])