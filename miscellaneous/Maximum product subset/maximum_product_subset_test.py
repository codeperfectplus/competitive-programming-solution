from maximum_product_subset import max_product

import unittest


class MaxProductTest(unittest.TestCase):

    def test_max_prodcut_1(self):
        self.assertEqual(max_product([1, -2, -3, 4, 5]), 120)

    def test_max_prodcut_2(self):
        self.assertEqual(max_product([]), 0)

    def test_max_prodcut_3(self):
        self.assertEqual(max_product([6]), 6)

    def test_max_product_4(self):
        self.assertEqual(max_product([1, 2, -4, 6]), 12)

    def test_max_product_5(self):
        self.assertEqual(max_product([-1, -2, -3, 4, 5]), 120)

    def test_max_product_6(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), 120)

    def test_max_product_7(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5, -6]), 720)

    def test_max_product_8(self):
        self.assertEqual(max_product([-2, -3, 1, -2]), 6)

    def test_max_product_9(self):
        self.assertEqual(max_product([-2, -3, -2, -2]), 24)

    def test_max_product_10(self):
        self.assertEqual(max_product([-2, -3, -1]), 6)


if __name__ == '__main__':
    unittest.main()
