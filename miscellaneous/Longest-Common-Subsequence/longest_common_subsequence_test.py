from longest_common_subsequence import lcs

import unittest

class LcsTest(unittest.TestCase):
    def test_1(self):
        X = "DCBABDB"
        Y = "CAB"
        self.assertEqual(lcs(X, Y, len(X), len(Y)), 3)

if __name__ == '__main__':
    unittest.main()
