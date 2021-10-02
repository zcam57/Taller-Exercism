def is_pangram(frase):
    resultado = set()
    for x in frase.lower():
        if x.isalpha():
            resultado.add(x)
    return len(resultado) == 26