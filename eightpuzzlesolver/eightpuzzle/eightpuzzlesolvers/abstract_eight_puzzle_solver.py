from abc import ABC, abstractmethod
from timeit import default_timer as timer


class AbstractEightPuzzleSolver(ABC):
    """An abstract class for an eight digit puzzle solver"""

    @abstractmethod
    def solve_eight_puzzle(self, eight_puzzle):
        """Solves the given eight digit puzzle

        Args:
            eight_puzzle (EightPuzzle): The eight digit puzzle to solve.

        Returns:
            list: Returns a list of states to solve a board (get the current state to the goal state of 0123456789).

        """
        pass

    def time_solve(self, eight_puzzle):
        """

        Args:
            eight_puzzle (EightPuzzle): The eight digit puzzle to solve.

        Returns:
            float: Returns the time in seconds that the eight puzzle solver took to solve a board.

        """
        start = timer()
        self.solve_eight_puzzle(eight_puzzle)
        end = timer()
        return end - start
