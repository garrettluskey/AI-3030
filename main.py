from board import Board
from searches import greedy_search, calculate_heuristic_value, bfs

#for x in greedy_search(Board(board=[[1,0,3], [4,5,6], [7,8,2]])):
 #   print(x)


bfs(Board(board=[[0,2,3], [4,5,3], [7,8,1]]))
# for x in bfs(Board(board=[[1,2,3], [4,5,3], [7,8,6]])):
#     print(x)