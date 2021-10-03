def square_of_sum(numero):
     return sum(i for i in range(1, numero + 1)) ** 2

def sum_of_squares(numero):
    return sum(i ** 2 for i in range(1, numero + 1))


def difference_of_squares(numero):
    return square_of_sum(numero) - sum_of_squares(numero)
