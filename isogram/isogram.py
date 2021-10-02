def is_isogram(palabra):
  letras = [x for x in palabra.lower() if "a" <= x <= "z"]
  return len(letras) == len(set(letras))