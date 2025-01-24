import unittest
from hw3 import find_pairs_naive, find_pairs_optimized

#Test naive
class Testhw3(unittest.TestCase):

    def testnaive(self):
        actual = find_pairs_naive([1,2,3,4,5,6,7,8,9], 10)
        expected = {(1, 9), (2, 8), (3, 7), (4,6)}
        self.assertEqual(actual, expected)

        actual2 = find_pairs_naive([1,2,3,4,5], 10)
        expected2 = set()
        self.assertEqual(actual2, expected2)

        actual3 = find_pairs_naive([], 10)
        expected3 = set()
        self.assertEqual(actual3, expected3)

    def testoptimized(self):
        actual = find_pairs_optimized([1,2,3,4,5,6,7,8,9], 10)
        expected = {(1, 9), (2, 8), (3, 7), (4,6)}
        self.assertEqual(actual, expected)

        actual2 = find_pairs_optimized([1,2,3,4,5], 10)
        expected2 = set()
        self.assertEqual(actual2, expected2)

        actual3 = find_pairs_optimized([], 10)
        expected3 = set()
        self.assertEqual(actual3, expected3)

unittest.main()
