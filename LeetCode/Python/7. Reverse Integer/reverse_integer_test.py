import unittest

from reverse_integer import Solution

obj = Solution()

class ReverseIntegerTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(obj.reverse(123), 321)

    def test_two(self):
        self.assertEqual(obj.reverse(1534236469), 0)
    
    def test_three(self):
        self.assertEqual(obj.reverse(120), 21)

    def test_four(self):
        self.assertEqual(obj.reverse(0), 0)

if __name__ == '__main__':
    unittest.main()