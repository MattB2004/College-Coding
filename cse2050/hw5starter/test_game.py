import unittest
import game
import maze

class TestGame(unittest.TestCase):

    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        finish = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, finish)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here
    def test2(self):
        grid = maze.Maze(2, 2)
        grid._set_maze([[2, 7]
                        [1, 3]])
        start = (0,0)
        finish = (1,1)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        self.assertEqual(score, 7)
        self.assertEqual(path, [(0,0),(0,1),(1,1)])

    def test3(self):
        grid = maze.Maze(2, 2)
        grid._set_maze([[2, '*']
                        ['*', 3]])
        start = (0,0)
        finish = (1,1)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        self.assertEqual(score, -1)
        self.assertEqual(path, [])
if __name__ == '__main__':
    unittest.main()
