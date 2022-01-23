"""
    Topic :
        Project Euler

    Problem Statement :
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import gcd
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

from functools import reduce

result = reduce(lcm, range(1,11))
print(result)