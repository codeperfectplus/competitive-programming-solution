from longest_collatz_sequence import solver

import unittest

class TestLongestCollatzSequence(unittest.TestCase):
    #def test_solver(self):
        #self.assertEqual(solver(1_000_000), 837799)
    
    def test_solver_2(self):
        self.assertEqual(solver(10), 9)


if __name__ == '__main__':
    unittest.main()