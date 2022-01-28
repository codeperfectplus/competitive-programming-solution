""" 
Title: Highly divisible triangular number

 """
from collections import defaultdict

def triangular_number(n):
    """
    Returns the nth triangular number.
    """
    return int(n * (n+1) / 2)

def get_factors(num):
    factors = defaultdict(list)
    factors[num].append(num)
    for i in range(1, num//2+1):
        if num % i == 0:
            factors[num].append(i)
    
    return num, len(factors[num])

def get_factors_length(num):
    for i in range(1, num):
        seq = triangular_number(i)
        seq, length = get_factors(seq)
        print(seq, length)

    return seq, length

print(get_factors_length(28))
