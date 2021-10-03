def sum_of_multiples(n, numeros=[3, 5]):
  
    def has_factors(k):
        
        return any(k % i == 0 for i in numeros if i)
    return sum(filter(has_factors, range(1, n)))