import random
import copy
import os
import math


class Board:
    __BOARD_WIDTH = 3
    __BOARD_HEIGHT = 3
    __SCRAMBLE_ITERATIONS = 1000
    completed_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, board=None):
        if not board:
            self.board = self.completed_board
            return
        if not self.__check_board_valid(board):
            raise ValueError("The given board is not valid")
        self.board = copy.deepcopy(board)
        if not self.__is_solvable():
            raise ValueError("The given board is not solvable")

    def __str__(self):
        value = ""
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                value += str(self.board[y][x]) if self.board[y][x] else " "
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

    def __count_inversions(self):
        inversion_count = 0
        for i in range(self.__BOARD_WIDTH * self.__BOARD_HEIGHT - 1):
            for j in range(i + 1, self.__BOARD_WIDTH * self.__BOARD_HEIGHT):
                current_value = self.board[math.floor(i / self.__BOARD_HEIGHT)][i % self.__BOARD_WIDTH]
                preceding_value = self.board[math.floor(j / self.__BOARD_HEIGHT)][j % self.__BOARD_WIDTH]
                if current_value > 0 and 0 < preceding_value < current_value:
                        inversion_count += 1
        return inversion_count

    def __is_solvable(self):
        return self.__count_inversions() % 2 == 0

    def scramble(self):
        for x in range(self.__SCRAMBLE_ITERATIONS):
            self.board = random.choice(self.calculate_child_states()).board

    def get_current_state(self):
        return copy.deepcopy(self.board)

    def move_up(self, cursor=None):
        if cursor:
            x, y = cursor
        else:
            x, y = self.__find_cursor()
        if y == self.__BOARD_HEIGHT - 1:
            return None
        board = self.get_current_state()
        board[y][x] = board[y + 1][x]
        board[y + 1][x] = 0
        return Board(board)

    def move_down(self, cursor=None):
        if cursor:
            x, y = cursor
        else:
            x, y = self.__find_cursor()
        if y == 0:
            return None
        board = self.get_current_state()
        board[y][x] = board[y - 1][x]
        board[y - 1][x] = 0
        return Board(board)

    def move_left(self, cursor=None):
        if cursor:
            x, y = cursor
        else:
            x, y = self.__find_cursor()
        if x == self.__BOARD_WIDTH - 1:
            return None
        board = self.get_current_state()
        board[y][x] = board[y][x + 1]
        board[y][x + 1] = 0
        return Board(board)

    def move_right(self, cursor=None):
        if cursor:
            x, y = cursor
        else:
            x, y = self.__find_cursor()
        if x == 0:
            return None
        board = self.get_current_state()
        board[y][x] = board[y][x - 1]
        board[y][x - 1] = 0
        return Board(board)

    def __find_cursor(self):
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                if self.board[y][x] == 0:
                    return x, y
        return None

    def num_misplaced(self):
        count = 0
        for i, x in enumerate(self.board):
            for j in range(len(x)):
                if self.board[i][j] != Board.completed_board[i][j]:
                    count += 1
        return count

    def is_won(self):
        if self.board == Board.completed_board:
            return True
        else:
            return False

    def calculate_child_states(self):
        cursor = self.__find_cursor()
        return list(filter(None, [self.move_up(cursor),
                                  self.move_down(cursor),
                                  self.move_left(cursor),
                                  self.move_right(cursor)]))
