from factorial_digit_sum import factorial_digit_sum

import unittest


class FactorialDigitSumTest(unittest.TestCase):

    def test_factorial_digit_sum_1(self):
        self.assertEqual(factorial_digit_sum(10), 27)

    def test_factorial_digit_sum_2(self):
        self.assertEqual(factorial_digit_sum(100), 648)


if __name__ == '__main__':
    unittest.main()
