from knapsack import knapsack

import unittest

class KnapsackTest(unittest.TestCase):

    def test_knapsack_1(self):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        max_capacity = 50
        self.assertEqual(knapsack(val, wt, max_capacity), 240)


if __name__ == '__main__':
    unittest.main()
