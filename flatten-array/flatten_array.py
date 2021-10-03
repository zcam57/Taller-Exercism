def flatten(iterable):
    lista = []
    for valor in iterable:
        if isinstance(valor, list):
            lista.extend(flatten(valor))
        elif valor != None:
            lista.append(valor)
    return lista