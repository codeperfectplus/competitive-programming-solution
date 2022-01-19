from max_activity import getMaxActivities
import unittest

class MaxActivitiesTest(unittest.TestCase):

    def test1(self):
        start  = [10, 12, 20]
        finish = [20, 25, 30]
        self.assertEqual(getMaxActivities(start, finish), [0, 2]) 

    def test2(self):
        start  = [1, 3, 0, 5, 8, 5]
        finish = [2, 4, 6, 7, 9, 9]
        self.assertEqual(getMaxActivities(start, finish), [0, 1, 3, 4])

if __name__ == '__main__':
    unittest.main()