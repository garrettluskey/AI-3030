import random
import copy
import os
import math


class Board:
    '''
    Board State Class

    This class stores the state of a 8-puzzle by using
    a 2d array to store the state of the game and having
    methods to manipulate the array.

    Args:
        board (2d list): ex [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            if not given a random board will be generated    
    '''
    __BOARD_WIDTH = 3
    __BOARD_HEIGHT = 3
    __SCRAMBLE_ITERATIONS = 1000
    completed_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, board=None):
        '''Board constructor
           If no board is given, the constuctor will create a random board
        '''
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

    def get_board_width(self):
        return self.__BOARD_WIDTH

    def get_board_height(self):
        return self.__BOARD_HEIGHT

    def __check_board_valid(self, board):
        ''' Verifies if given board is valid.
            Returns true if board is valid, false if not.
        '''
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
        ''' Counts inversions for if board is solvable.
            Returns number of inversions.
        '''
        inversion_count = 0
        for i in range(self.__BOARD_WIDTH * self.__BOARD_HEIGHT - 1):
            for j in range(i + 1, self.__BOARD_WIDTH * self.__BOARD_HEIGHT):
                current_value = self.board[math.floor(i / self.__BOARD_HEIGHT)][i % self.__BOARD_WIDTH]
                preceding_value = self.board[math.floor(j / self.__BOARD_HEIGHT)][j % self.__BOARD_WIDTH]
                if current_value > 0 and 0 < preceding_value < current_value:
                        inversion_count += 1
        return inversion_count

    def __is_solvable(self):
        ''' Verifies if the board is solvable.'''
        return self.__count_inversions() % 2 == 0

    def scramble(self):
        ''' Scrambles board randomly.'''
        for x in range(self.__SCRAMBLE_ITERATIONS):
            self.board = random.choice(self.calculate_child_states()).board

    def get_current_state(self):
        ''' Returns a copy of the board array.'''
        return copy.deepcopy(self.board)

    def move_up(self, cursor=None):
        ''' Moves the empty block 1 place up.
            Returns None if the empty block is on the top.
            Otherwise returns new Board object with move.
        '''
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
        ''' Moves the empty block 1 place down.
            Returns None if the empty block is on the bottom.
            Otherwise returns new Board object with move.
        '''
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

    def move_right(self, cursor=None):
        ''' Moves the empty block 1 place to the right.
            Returns None if the empty block is on the far right.
            Otherwise returns new Board object with move.
        '''
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

    def move_left(self, cursor=None):
        ''' Moves the empty block 1 place to the left.
            Returns None if the empty block is on the far left.
            Otherwise returns new Board object with move.
        '''
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
        ''' Return the x, y coordinates of the empty position on the board.'''
        for y in range(self.__BOARD_HEIGHT):
            for x in range(self.__BOARD_WIDTH):
                if self.board[y][x] == 0:
                    return x, y
        return None

    def num_misplaced(self):
        ''' Returns number of tiles that are not in the solved position.'''
        count = 0
        for i, x in enumerate(self.board):
            for j in range(len(x)):
                if self.board[i][j] != Board.completed_board[i][j]:
                    count += 1
        return count

    def is_won(self):
        ''' Returns if the game is in a completed state.'''
        if self.board == Board.completed_board:
            return True
        else:
            return False

    def calculate_child_states(self):
        ''' Returns a list of Board objects for each valid move from given state.'''
        cursor = self.__find_cursor()
        return list(filter(None, [self.move_up(cursor),
                                  self.move_down(cursor),
                                  self.move_left(cursor),
                                  self.move_right(cursor)]))
