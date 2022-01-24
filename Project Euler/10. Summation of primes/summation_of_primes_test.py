from summation_of_primes import main

import unittest

class SumOfPrimes(unittest.TestCase):
    def test_sum_of_primes_1(self):
        self.assertEqual(main(10), 17)
    

    def test_sum_of_primes_2(self):
        self.assertEqual(main(2000000), 142913828922)


if __name__ == '__main__':
    unittest.main()