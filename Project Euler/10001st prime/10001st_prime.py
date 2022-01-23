"""
Topic : 10001st prime
Problem Statement : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
                    we can see that the 6th prime is 13. What is the 10_001st prime number?
"""
import itertools
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True


p = 0
for x in itertools.count(1):
    if is_prime(x):
        if p == 10001:
            print("10001st prime is: ", x)
            break
        p += 1
         
# Answer: 104743