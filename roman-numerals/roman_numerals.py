romanos={
        1000: "M",
        900:  "CM",
        500:  "D",
        400:  "CD",
        100:  "C",
        90:   "XC",
        50:   "L",
        40:   "XL",
        10:   "X",
        9:    "IX",
        5:    "V",
        4:    "IV",
        1:    "I"}
def roman(numero):
    respuesta = ""
    for n, numeral in reversed(sorted(romanos.items())):
        if numero >= n:
            respuesta += (numero // n) * numeral
            numero = numero % n
    return respuesta