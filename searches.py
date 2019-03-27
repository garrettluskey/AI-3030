from board import Board
from queue import PriorityQueue
from math import sqrt, floor

def greedy_search(initial_state):
    queue = PriorityQueue()
    visited = []
    queue.put(HeuristicNode(calculate_heuristic_value(initial_state.board), initial_state))
    while not queue.empty():
        currentNode = queue.get()
        print(currentNode.item)
        if currentNode.item.board in visited:
            continue
        visited.append(currentNode.item.board)
        if currentNode.item.board == Board.completed_board:
            path = []
            while currentNode != None:
                path.insert(0, currentNode.item)
                currentNode = currentNode.parent
            return path
        for child_state in currentNode.item.calculate_child_states():
            if child_state.board not in visited: #check this again here because queue get and put is expensive
                queue.put(HeuristicNode(calculate_heuristic_value(child_state.board), child_state, currentNode))
    raise Exception("ouch")

class HeuristicNode:
    def __init__(self, heuristic, item, parent=None):
        self.heuristic = heuristic
        self.item = item
        self.parent = parent

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
            goalx = (val - 1) % 3
            goaly = floor((val - 1) / 3)
            heuristic_sum += sqrt((goalx - x)**2 + (goaly - y)**2) # distance from goal state
    return heuristic_sum