from power_digit_sum import solver

import unittest

class PowerDigitSumTest(unittest.TestCase):
    
    def test_power_digit_sum_1(self):
        self.assertEqual(solver(2, 15), 26)

    def test_power_digit_sum_2(self):
        self.assertEqual(solver(2, 1000), 1366)


if __name__ == '__main__':
    unittest.main()