from parallel_universe import minimumCost

import unittest

class ParallelUniverseTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(minimumCost(4, [8, 4, 0, 4]), 8)
    
    def test_case_2(self):
        self.assertEqual(minimumCost(4, [0, 40, 0, 0]), 60)

    def test_case_3(self):
        self.assertEqual(minimumCost(5, [1, 1, 1, 1, 1]), 0)


if __name__ == '__main__':
    unittest.main()