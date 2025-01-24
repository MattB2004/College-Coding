from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                board = [1, 2, 6, 1, 0]
                
                self.assertEqual(puzzle(board), True)

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                board = [3, 4, 7, 4, 1, 0]
                self.assertEqual(puzzle(board), True)
        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                board = [3, 5, 2, 4, 1, 0]
                self.assertEqual(puzzle(board), True)
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                board = [3, 5, 5]
                self.assertEqual(puzzle(board), False)
unittest.main()