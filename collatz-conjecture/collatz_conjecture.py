def steps(numero):
  if numero < 1:
    raise ValueError('Illegal input')
  steps = 0
  while numero != 1:
    if numero % 2 == 0:
      numero = numero / 2
    else:
      numero = (3 * numero) + 1
    steps += 1
  return steps