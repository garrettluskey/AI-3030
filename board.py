import random, copy
class Board:
    def __init__(self, board=None):
        Board.completed_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if board:
            self.board = copy.deepcopy(board)
        else:
            self.board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
            self.scramble()

    def __str__(self):
        output = ""
        for x in self.board:
            for y in x:
                if y == 0:
                    output += ' ' + ' '
                else:
                    output += str(y) + ' '
            output += '\n'
        return output

    def scramble(self):
        for i in range(random.randint(0, 100)):
            try:
                choice = random.randint(1,4)
                if choice == 1:
                    self.move_up()
                elif choice == 2:
                    self.move_down()
                elif choice == 3:
                    self.move_left()
                elif choice == 4:
                    self.move_right()
            except RuntimeWarning:
                i += 1

    def move_up(self):
        i, j = self._find_cursor()
        if i == 0:
            raise RuntimeWarning("Cursor at top")
        else:
            self._swap(i, j, i - 1, j)

    def move_down(self):
        i, j = self._find_cursor()
        if i == 2:
            raise RuntimeWarning("Cursor at bottom")
        else:
            self._swap(i, j, i + 1, j)

    def move_left(self):
        i, j = self._find_cursor()
        if j == 0:
            raise RuntimeWarning("Cursor at left wall")
        else:
            self._swap(i, j, i, j - 1)

    def move_right(self):
        i, j = self._find_cursor()
        if j == 2:
            raise RuntimeWarning("Cursor at right wall")
        else:
            self._swap(i, j, i, j + 1)

    def _swap(self, first_width, first_height, second_width, second_height):
        tmp = self.board[first_width][first_height]
        self.board[first_width][first_height] = self.board[second_width][second_height]
        self.board[second_width][second_height] = tmp

    def _find_cursor(self):
        for i, x in enumerate(self.board):
            for j, y in enumerate(x):
                if y == 0:
                    return (i, j)

    def num_misplaced(self):
        count = 0
        for i, x in enumerate(self.board):
            for j in range(len(x)):
                if(self.board[i][j] != Board.completed_board[i][j]):
                    count += 1
        return count


    def is_won(self):
        if self.board == Board.completed_board:
            return True
        else:
            return False

    def calculate_child_states(self):
        children = []
        for choice in range(1,5):
            try:
                if choice == 1:
                    child = Board(board=self.board)
                    child.move_up()
                elif choice == 2:
                    child = Board(board=self.board)
                    child.move_down()
                elif choice == 3:
                    child = Board(board=self.board)
                    child.move_left()
                elif choice == 4:
                    child = Board(board=self.board)
                    child.move_right()
                children.append(child)
            except RuntimeWarning:
                pass
        return children