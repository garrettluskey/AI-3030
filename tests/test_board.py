import unittest
from board import Board
import os


class TestBoard(unittest.TestCase):
    def test_eight_puzzle(self):
        # Test valid
        try:
            Board([[0, 1, 3], [2, 4, 6], [5, 7, 8]])
        except ValueError:
            self.fail()
        # Test invalid (extra 1)
        try:
            Board([[0, 1, 1], [2, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (missing 2)
        try:
            Board([[0, 1, 3], [9, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (wrong size)
        try:
            Board([[0, 1, 3], [2, 4, 6], [5, 7, 8, 9]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (wrong type)
        try:
            Board([[0, 1, 3.7], [2, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test random puzzle
        try:
            self.assertListEqual(Board().get_current_state(), Board.completed_board)
        except ValueError:
            self.fail()

    def test___str__(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        self.assertEqual(str(Board(state)), "4 1 3{0}2   6{0}5 8 7".format(os.linesep))

    def test_scramble(self):
        # Generate 8 random puzzles and see if any fail
        try:
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
            Board(Board().scramble())
        except ValueError:
            self.fail()

    def test_get_current_state(self):
        state = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        puzzle = Board(state)
        self.assertListEqual(state, puzzle.get_current_state())

    def test_calculate_child_states(self):
        state1 = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        self.assertEqual(len(Board(state1).calculate_child_states()), 2)
        state2 = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        self.assertEqual(len(Board(state2).calculate_child_states()), 4)

    def test_move_up(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        up = [[4, 1, 3], [2, 8, 6], [5, 0, 7]]
        self.assertListEqual(Board(state).move_up().get_current_state(), up)

    def test_move_down(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        down = [[4, 0, 3], [2, 1, 6], [5, 8, 7]]
        self.assertListEqual(Board(state).move_down().get_current_state(), down)

    def test_move_left(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        left = [[4, 1, 3], [2, 6, 0], [5, 8, 7]]
        self.assertListEqual(Board(state).move_left().get_current_state(), left)

    def test_move_right(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 8, 7]]
        right = [[4, 1, 3], [0, 2, 6], [5, 8, 7]]
        self.assertListEqual(Board(state).move_right().get_current_state(), right)
