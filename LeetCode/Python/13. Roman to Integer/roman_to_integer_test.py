import unittest

from roman_to_integer import Solution

obj = Solution()

class RomanToIntegerTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(obj.romanToInt('III'), 3)

    def test_two(self):
        self.assertEqual(obj.romanToInt('IV'), 4)

    def test_three(self):
        self.assertEqual(obj.romanToInt('IX'), 9)

    def test_four(self):
        self.assertEqual(obj.romanToInt('LVIII'), 58)

    def test_five(self):
        self.assertEqual(obj.romanToInt('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()
