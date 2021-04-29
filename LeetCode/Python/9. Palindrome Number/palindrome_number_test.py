import unittest

from palindrome_number import Solution

obj = Solution()


class PalinDromeNumberTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(obj.isPalindrome(121), True)

    def test_two(self):
        self.assertFalse(obj.isPalindrome(-121), False)

    def test_three(self):
        self.assertTrue(obj.isPalindrome(0), True)

    def test_fout(self):
        self.assertFalse(obj.isPalindrome(10), False)


if __name__ == '__main__':
    unittest.main()
