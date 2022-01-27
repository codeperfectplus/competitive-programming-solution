""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def sum_of_primes(num):
    for x in range(2, num+1):
        half = int(sqrt(x)) + 1
        for y in range(2, half):
            if x % y == 0:
                break
        else:
            yield x


def main(num):
    return sum([x for x in sum_of_primes(num)])

# REVIEW: Need to be optimized.