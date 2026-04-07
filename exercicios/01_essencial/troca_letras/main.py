def resposta (s):
    s = str(s)

    if len(s) <= 1:
        return s
    else:
        primeiro_carac = s[0]
        ultimo_carac = s[-1]

        palavra = ultimo_carac + s[1:-1] + primeiro_carac

        return palavra
