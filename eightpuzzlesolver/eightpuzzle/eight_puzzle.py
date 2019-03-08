# Probably going to be going to be composed of a current state
# and a 2d array with top left being (0, 0) and bottom right 
# being (2, 2)


class EightPuzzle:
    __eight_puzzle = [[0 for i in range(3)] for j in range(3)]

    def get_current_state(self):
        return self.__eight_puzzle.copy()
