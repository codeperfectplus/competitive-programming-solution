"""
Topic : 10001st prime
Problem Statement : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
                    we can see that the 6th prime is 13. What is the 10_001st prime number?
"""
from prime_10001 import main

import unittest

class Test10001stPrime(unittest.TestCase):

    def test_10001st_prime(self):
        self.assertEqual(main(10001), 104743)


if __name__ == "__main__":
    unittest.main()