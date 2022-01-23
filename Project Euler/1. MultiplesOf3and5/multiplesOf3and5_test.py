from multiplesOf3and5 import sum_of_multiples

import unittest

class SumOfMultiple(unittest.TestCase):
    def test_sum_of_multiples_1(self):
        self.assertEqual(sum_of_multiples(10), 23)

    def test_sum_of_multiples_2(self):
        self.assertEqual(sum_of_multiples(1000), 233168)