""" The four adjacent digits in the 1000-digit number 
that have the greatest product are 9 × 9 × 8 × 9 = 5832. 

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""
from functools import reduce
from operator import mul

def find_largest_product(big_num, m):
    integers = [int(character) for character in big_num]
    # print(integers)
    n = len(integers)
    answer = 0

    for i in range(n - m + 1):
        subset = integers[i:i+m]
        product = reduce(mul, subset, 1)
        answer = max(answer, product)

    return answer
