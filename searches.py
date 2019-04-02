from board import Board
from math import sqrt, floor
import time


def bfs(initial_state, timeout=30):
    initial_time = time.time()
    open_list = []
    temp = (initial_state, None)
    final = None
    while not final and (time.time() - initial_time) < timeout:
        if temp[0].board == Board.completed_board:
            final = temp
        else:
            for x in temp[0].calculate_child_states():
                open_list.append((x, temp))
            temp = open_list.pop(0)
    if (time.time() - initial_time) < timeout:
        return []  # if it's an error return an empty list so it can be handled easier
    final_arr = []
    while final[1]:
        final_arr.append(final[0])
        final = final[1]
    final_arr.reverse()
    for x in final_arr:
        print(x)


def greedy_search(initial_state):
    queue = []
    visited = []
    queue.append(HeuristicNode(calculate_heuristic_value(initial_state.board), initial_state))
    while queue:
        current_node = get_smallest_and_remove(queue)
        if current_node.item.board in visited:
            continue
        visited.append(current_node.item.board)
        if current_node.item.board == Board.completed_board:
            path = []
            while current_node:
                path.insert(0, current_node.item)
                current_node = current_node.parent
            return path
        for child_state in current_node.item.calculate_child_states():
            queue.append(HeuristicNode(calculate_heuristic_value(child_state.board), child_state, current_node))
    return []


def a_star_search(initial_state):
    queue = []
    visited = []
    queue.append(HeuristicNode(calculate_heuristic_value(initial_state.board), initial_state))
    while queue:
        current_node = get_smallest_and_remove(queue)
        if current_node.item.board in visited:
            continue
        visited.append(current_node.item.board)
        if current_node.item.board == Board.completed_board:
            path = []
            while current_node:
                path.insert(0, current_node.item)
                current_node = current_node.parent
            return path
        for child_state in current_node.item.calculate_child_states():
            queue.append(
                HeuristicNode(calculate_heuristic_value(child_state.board) + current_node.depth + 1, child_state,
                              current_node, current_node.depth + 1))
    return[]


def get_smallest_and_remove(queue):
    if not queue:
        return None
    index = 0
    current_node = queue[0]
    for i in range(len(queue)):
        if queue[i].heuristic < current_node.heuristic:
            current_node = queue[i]
            index = i
    del queue[index]
    return current_node


class HeuristicNode:
    def __init__(self, heuristic, item, parent=None, depth=0):
        self.heuristic = heuristic
        self.item = item
        self.parent = parent
        self.depth = depth

    def __gt__(self, heuristic_node):
        return self.heuristic > heuristic_node.heuristic

    def __lt__(self, heuristic_node):
        return self.heuristic < heuristic_node.heuristic


def calculate_heuristic_value(board):
    heuristic_sum = 0
    for y in range(3):
        for x in range(3):
            val = board[y][x]
            if val == 0:
                val = 9
            goal_x = (val - 1) % 3
            goal_y = floor((val - 1) / 3)
            heuristic_sum += sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)  # distance from goal state
    return heuristic_sum
