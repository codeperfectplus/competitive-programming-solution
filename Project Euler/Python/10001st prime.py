"""
    Topic : 
    Problem Statement :
                    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
                        What is the 10 001st prime number?
"""
import itertools


def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
        else:
            continue
    return True


p = 0
for x in itertools.count(1):
    if is_prime(x):
        if p == 10001:
            print(x)
            break
        p += 1
         
