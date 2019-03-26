import unittest
from .. import EightPuzzle
import os


class TestEightPuzzle(unittest.TestCase):
    def test_eight_puzzle(self):
        # Test valid
        try:
            EightPuzzle([[0, 1, 3], [2, 4, 6], [5, 7, 8]])
        except ValueError:
            self.fail()
        # Test invalid (extra 1)
        try:
            EightPuzzle([[0, 1, 1], [2, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (missing 2)
        try:
            EightPuzzle([[0, 1, 3], [9, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (wrong size)
        try:
            EightPuzzle([[0, 1, 3], [2, 4, 6], [5, 7, 8, 9]])
            self.fail()
        except ValueError:
            pass
        # Test invalid (wrong type)
        try:
            EightPuzzle([[0, 1, 3.7], [2, 4, 6], [5, 7, 8]])
            self.fail()
        except ValueError:
            pass
        # Test random puzzle
        try:
            EightPuzzle()
        except ValueError:
            self.fail()

    def test___str__(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        self.assertEqual(str(EightPuzzle(state)), "4 1 3{0}2 0 6{0}5 7 8".format(os.linesep))

    def test_generate_random_board(self):
        # Generate 8 random puzzles and see if any fail
        try:
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
            EightPuzzle(EightPuzzle().get_current_state())
        except ValueError:
            self.fail()

    def test_get_current_state(self):
        state = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        puzzle = EightPuzzle(state)
        self.assertListEqual(state, puzzle.get_current_state())

    def test_find_zero_coord(self):
        state1 = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        self.assertTupleEqual((0, 0), EightPuzzle(state1).find_zero_coord())
        state2 = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        self.assertTupleEqual((1, 1), EightPuzzle(state2).find_zero_coord())
        state3 = [[8, 1, 3], [2, 4, 6], [5, 7, 0]]
        self.assertTupleEqual((2, 2), EightPuzzle(state3).find_zero_coord())
        state3 = [[8, 1, 0], [2, 4, 6], [5, 7, 3]]
        self.assertTupleEqual((2, 0), EightPuzzle(state3).find_zero_coord())

    def test_calculate_future_states(self):
        state1 = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        self.assertEqual(len(EightPuzzle(state1).calculate_future_states()), 2)
        state2 = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        self.assertEqual(len(EightPuzzle(state2).calculate_future_states()), 4)

    def test_calculate_move_up(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        up = [[4, 1, 3], [2, 7, 6], [5, 0, 8]]
        self.assertListEqual(EightPuzzle(state).calculate_move_up(), up)

    def test_calculate_move_down(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        down = [[4, 0, 3], [2, 1, 6], [5, 7, 8]]
        self.assertListEqual(EightPuzzle(state).calculate_move_down(), down)

    def test_calculate_move_left(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        left = [[4, 1, 3], [2, 6, 0], [5, 7, 8]]
        self.assertListEqual(EightPuzzle(state).calculate_move_left(), left)

    def test_calculate_move_right(self):
        state = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        right = [[4, 1, 3], [0, 2, 6], [5, 7, 8]]
        self.assertListEqual(EightPuzzle(state).calculate_move_right(), right)

    def test_calculate_heuristic_value(self):
        state1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        state2 = [[0, 2, 1], [3, 4, 5], [6, 7, 8]]
        state3 = [[4, 1, 3], [2, 0, 6], [5, 7, 8]]
        state4 = [[0, 1, 3], [2, 4, 6], [5, 7, 8]]
        self.assertEqual(EightPuzzle(state1).calculate_heuristic_value(), 0)
        self.assertGreater(EightPuzzle(state2).calculate_heuristic_value(),
                           EightPuzzle(state1).calculate_heuristic_value())
        self.assertLess(EightPuzzle(state4).calculate_heuristic_value(),
                        EightPuzzle(state3).calculate_heuristic_value())
