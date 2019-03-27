from board import Board
from searches import greedy_search, calculate_heuristic_value

for x in greedy_search(Board(board=[[1,0,3], [4,5,6], [7,8,2]])):
    print(x)