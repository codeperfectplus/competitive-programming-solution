from count_occurrences import count_occurrences_function

import unittest

class CountOccurrenceTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_occurrences_function('a'), {'a': 1})
    
    def test_2(self):
        self.assertEqual(count_occurrences_function('aa'), {'a': 2})

    def test_3(self):
        self.assertEqual(count_occurrences_function('aaa'), {'a': 3})
    
    def test_4(self):
        self.assertEqual(count_occurrences_function('aaaa'), {'a': 4})
    
    def test_5(self):
        self.assertEqual(count_occurrences_function('abcdABCD'), {'a': 2, 'b': 2, 'c': 2, 'd': 2})
    
    def test_6(self):
        self.assertEqual(count_occurrences_function('abcdABCDabcdABCD'), {'a': 4, 'b': 4, 'c': 4, 'd': 4})
    

if __name__ == '__main__':
    unittest.main()