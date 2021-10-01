def latest(puntaje):
    return puntaje[-1]

def personal_best(puntaje):
    return max(puntaje)


def personal_top_three(puntaje):
    orden = sorted(puntaje, reverse=True)
    return orden[0:3]