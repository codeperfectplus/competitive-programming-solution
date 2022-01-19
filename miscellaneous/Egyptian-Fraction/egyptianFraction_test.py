from egyptian_fraction import egyptianFraction

import unittest

class EgyptianFractionTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(egyptianFraction(0, 2), [])
    
    def test2(self):
        self.assertEqual(egyptianFraction(4, 3), [])

    def test3(self):
        self.assertEqual(egyptianFraction(2, 3), [2, 6])

    def test4(self):
        self.assertEqual(egyptianFraction(6, 14), [3, 11, 231])

    def test5(self):
        self.assertEqual(egyptianFraction(0, 0), [])
if __name__ == '__main__':
    unittest.main()
