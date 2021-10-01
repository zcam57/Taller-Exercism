def is_paired(llaves):
    abiertos = "[{("
    cerrados = "]})"
    monton = []
    for x in llaves:
        if x in abiertos:
            monton.append(x)
        elif x in cerrados:
            if not monton or abiertos[cerrados.index(x)] != monton.pop():
                return False
    return not monton