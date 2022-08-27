from compare_list import compare_list_function

import unittest

class CompareListTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compare_list_function([2, 1, 3, 5, 4], [1, 4, 9, 16, 25]), True)

    def test_2(self):
        self.assertEqual(compare_list_function([0, 0], [0, 2]), False)
    
    def test_3(self):
        self.assertEqual(compare_list_function([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), False)
    
    def test_4(self):
        self.assertEqual(compare_list_function([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), True)

if __name__ == '__main__':
    unittest.main()