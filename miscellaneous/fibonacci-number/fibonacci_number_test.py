from fibonacci_number import fibonacci_series
import unittest


class FibonacciSeriesTest(unittest.TestCase):
    
        def test1(self):
            self.assertEqual(fibonacci_series(10), 34)

        def test2(self):
            self.assertEqual(fibonacci_series(0), 0)
        
        def test3(self):
            self.assertEqual(fibonacci_series(1), 0)
        
        def test4(self):
            self.assertEqual(fibonacci_series(2), 1)
        
        def test5(self):
            self.assertEqual(fibonacci_series(3), 1)
        
        def test6(self):
            self.assertEqual(fibonacci_series(4), 2)
        
        def test7(self):
            self.assertEqual(fibonacci_series(5), 3)
        
        def test8(self):
            self.assertEqual(fibonacci_series(6), 5)    
        

if __name__ == '__main__':
    unittest.main()