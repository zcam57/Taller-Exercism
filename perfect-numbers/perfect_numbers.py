def classify(numero):
    if numero > 0:
        total = sum([x for x in range(1, numero) if numero % x == 0])
        if total == numero:
            return "perfect"
        if total > numero:
            return "abundant"
        if total < numero:
            return "deficient"
    else:
        raise ValueError("Invalid Input")