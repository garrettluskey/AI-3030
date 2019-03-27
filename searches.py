from board import Board
from queue import PriorityQueue
from math import sqrt, floor

def greedy_search(initial_state):
    queue = PriorityQueue()
    queue.put(-calculate_heuristic_value(initial_state.board), initial_state)
    closed = list()
    while not queue.empty():
        current = queue.get()[1]
        if current.board = goal_state:
            return list(queue.queue)
        elif current not in closed:
            closed.append(current)
            for child_state in current.calculate_child_states():
                queue.put(-calculate_heuristic_value(current.board), current)
    raise Exception("ouch")

def calculate_heuristic_value(board):
    heuristic_sum = 0
    for y in range(3):
        for x in range(3):
            val = board[y][x]
            if val == 0:
                val = 9
            heuristic_sum += sqrt((floor(val / 3) - x)^2 + (val % 3)^2) # distance from goal state