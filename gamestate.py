board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def move_up(board):
    i, j = find_cursor(board)
    if i == 0:
        raise RuntimeWarning("Cursor at top")
    else:
        swap(board, i, j, i - 1, j)

def move_down(board):
    i, j = find_cursor(board)
    if i == 2:
        raise RuntimeWarning("Cursor at bottom")
    else:
        swap(board, i, j, i + 1, j)

def move_left(board):
    i, j = find_cursor(board)
    if j == 0:
        raise RuntimeWarning("Cursor at left wall")
    else:
        swap(board, i, j, i, j - 1)

def move_right(board):
    i, j = find_cursor(board)
    if j == 2:
        raise RuntimeWarning("Cursor at right wall")
    else:
        swap(board, i, j, i, j + 1)

def swap(board, first_width, first_height, second_width, second_height):
    tmp = board[first_width][first_height]
    board[first_width][first_height] = board[second_width][second_height]
    board[second_width][second_height] = tmp
    print(board)

def find_cursor(board):
    for i, x in enumerate(board):
        for j, y in enumerate(x):
            if y == 0:
                return (i, j)

def is_won(board):
    if board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return True
    else:
        return False