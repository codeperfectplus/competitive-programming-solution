from minimum_product_subset import min_product

import unittest

class MinimumProductTest(unittest.TestCase):
    def test_minimum_product(self):
        self.assertEqual(min_product([]), 0)

    def test_minimum_product_1(self):
        self.assertEqual(min_product([50]), 50)

    def test_minimum_product_2(self):
        self.assertEqual(min_product([-1, -2, -3, -4, -5]), -120)
    
    def test_minimum_product_3(self):
        self.assertEqual(min_product([-1, -2, -3, -4, -5, -6]), -120)
    
    def test_minimum_product_4(self):
        self.assertEqual(min_product([-1, -2, -3, -4, -5, -6, 0]), 0)
    
    def test_minimum_product_5(self):
        self.assertEqual(min_product([90, 10, 20, 50, 80]), 10)
    
    def test_minimum_product_6(self):
        self.assertEqual(min_product([-6, -5]), -5)

if __name__ == '__main__':
    unittest.main()