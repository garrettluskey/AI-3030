# Probably going to be going to be composed of a current state
# and a 2d array with top left being (0, 0) and bottom right 
# being (2, 2)

import os
import random
import math


class EightPuzzle:
    __BOARD_WIDTH = 3
    __BOARD_HEIGHT = 3
    __board = None

    def __init__(self, board=None):
        if board is None:
            self.__board = self.generate_random_board()
            return
        if not self.__check_board_valid(board):
            raise ValueError("The given board is not valid")
        self.__board = board
        return

    def __str__(self):
        value = ""
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                value += str(self.__board[y][x])
                if x != self.__BOARD_WIDTH - 1:
                    value += " "
            if y != self.__BOARD_HEIGHT - 1:
                value += os.linesep
        return value

    def __check_board_valid(self, board):
        # check if board is list and is the proper width
        if type(board) != list or len(board) != self.__BOARD_HEIGHT:
            return False
        # create an empty list to contain the flattened elements of the board
        elements = []
        for y in range(self.__BOARD_HEIGHT):
            # check each sub element of the board is a list and is the proper height
            if type(board[y]) != list or len(board[y]) != self.__BOARD_WIDTH:
                return False
            for x in range(self.__BOARD_WIDTH):
                # check each element in the board is an integer
                if type(board[y][x]) != int:
                    return False
                # append element to flattened element list
                elements.append(board[y][x])
        # check that the elements are 0 through width * height
        elements.sort()
        if elements != list(range(self.__BOARD_HEIGHT * self.__BOARD_WIDTH)):
            return False
        return True

    def generate_random_board(self):
        elements = list(range(self.__BOARD_HEIGHT * self.__BOARD_WIDTH))
        random.shuffle(elements)
        eight_puzzle = []
        for y in range(self.__BOARD_HEIGHT):
            column = []
            for x in range(self.__BOARD_WIDTH):
                column.append(elements.pop())
            eight_puzzle.append(column)
        return eight_puzzle

    def get_current_state(self):
        copy = []
        for y in range(self.__BOARD_HEIGHT):
            copy.append(self.__board[y].copy())
        return copy

    def calculate_future_states(self):
        zero_coords = self.find_zero_coord()
        return list(filter(None, [self.calculate_move_up(zero_coords),
                                  self.calculate_move_down(zero_coords),
                                  self.calculate_move_left(zero_coords),
                                  self.calculate_move_right(zero_coords)]))

    def find_zero_coord(self):
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                if self.__board[y][x] == 0:
                    return x, y
        return None

    # If you swiped your finger from bottom to top (number below 0 swaps with 0)
    def calculate_move_up(self, zero_coords=None):
        if zero_coords is None:
            zero_coords = self.find_zero_coord()
        if zero_coords[1] == self.__BOARD_HEIGHT:
            return None
        board = self.get_current_state()
        board[zero_coords[1]][zero_coords[0]] = board[zero_coords[1] + 1][zero_coords[0]]
        board[zero_coords[1] + 1][zero_coords[0]] = 0
        return board

    # If you swiped your finger from top to bottom (number above 0 swaps with 0)
    def calculate_move_down(self, zero_coords=None):
        if zero_coords is None:
            zero_coords = self.find_zero_coord()
        if zero_coords[1] == 0:
            return None
        board = self.get_current_state()
        board[zero_coords[1]][zero_coords[0]] = board[zero_coords[1] - 1][zero_coords[0]]
        board[zero_coords[1] - 1][zero_coords[0]] = 0
        return board

    # If you swiped your finger from right to left (number right of 0 swaps with 0)
    def calculate_move_left(self, zero_coords=None):
        if zero_coords is None:
            zero_coords = self.find_zero_coord()
        if zero_coords[0] == self.__BOARD_WIDTH:
            return None
        board = self.get_current_state()
        board[zero_coords[1]][zero_coords[0]] = board[zero_coords[1]][zero_coords[0] + 1]
        board[zero_coords[1]][zero_coords[0] + 1] = 0
        return board

    # If you swiped your finger from left to right (number left of 0 swaps with 0)
    def calculate_move_right(self, zero_coords=None):
        if zero_coords is None:
            zero_coords = self.find_zero_coord()
        if zero_coords[1] == 0:
            return None
        board = self.get_current_state()
        board[zero_coords[1]][zero_coords[0]] = board[zero_coords[1]][zero_coords[0] - 1]
        board[zero_coords[1]][zero_coords[0] - 1] = 0
        return board

    def calculate_heuristic_value(self):
        sum_distances = 0
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                value = self.__board[y][x]
                sum_distances += math.sqrt(math.pow((math.floor(value / self.__BOARD_HEIGHT) - y), 2)
                                           + math.pow((value % self.__BOARD_WIDTH - x), 2))
        return sum_distances
