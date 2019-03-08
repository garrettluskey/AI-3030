import unittest
from eightpuzzle import EightPuzzle
from eightpuzzle.eightpuzzlesolvers import AStarEightPuzzleSolver


class TestAStarEightPuzzleSolver(unittest.TestCase):
    def test_solve_eight_puzzle(self):
        puzzle = EightPuzzle()
        puzzle_solver = AStarEightPuzzleSolver()
        puzzle_states = puzzle_solver.solve_eight_puzzle(puzzle)
        # self.assertListEqual(puzzle_states, [])
        self.fail("Not implemented")
