def resposta(dias, horas, minutos, segundos):
    dias = int(dias)
    horas = int(horas)
    minutos = int(minutos)
    segundos = int (segundos)

    resultado = ((dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos *60) + segundos)

    return (resultado)
