import unittest

from two_sum import Solution

obj = Solution()


class TwoSumTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(obj.two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two(self):
        self.assertEqual(obj.two_sum([1, 5, 6, 8], 14), [2, 3])


if __name__ == '__main__':
    unittest.main()
