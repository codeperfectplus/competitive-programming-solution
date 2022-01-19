from increasing_subarray import increasing_subarray

import unittest


class IncresingSubarray(unittest.TestCase):

    def test1(self):
        self.assertEqual(increasing_subarray([1, 2, 2, 4]), 2)
    
    def test2(self):
        self.assertEqual(increasing_subarray([1, 2, 5, 3, 4]), 3)
    
    def test3(self):
        self.assertEqual(increasing_subarray([1, 2]), 2)
    
    def test4(self):
        self.assertEqual(increasing_subarray([1, 2, 3, 4, 5]), 5)
    
    def test5(self):
        self.assertEqual(increasing_subarray([1, 2, 3, 4, 5, 6]), 6)
    
    def test6(self):
        self.assertEqual(increasing_subarray([2, 5, 6, 7, 5]), 4)

    def test7(self):
        self.assertEqual(increasing_subarray([2, 5, 6, 7, 5, 1]), 4)

if __name__ == '__main__':
    unittest.main()