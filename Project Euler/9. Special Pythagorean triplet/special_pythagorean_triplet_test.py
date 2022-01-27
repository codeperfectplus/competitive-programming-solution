from special_pythagorean_triplet import solver

import unittest

class TestSpecialPythagoreanTriplet(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(solver(1000), 31875000)


if __name__ == '__main__':
    unittest.main()