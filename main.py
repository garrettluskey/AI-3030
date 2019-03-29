from board import Board
from searches import greedy_search, a_star_search, bfs

print("a_star_search")
print("moves: {0}".format(len(a_star_search(Board(board=[[5, 1, 3], [4, 2, 6], [7, 8, 0]])))))
print("greedy_search")
print("moves: {0}".format(len(greedy_search(Board(board=[[5, 1, 3], [4, 2, 6], [7, 8, 0]])))))
print("bfs")
print("moves: {0}".format(len(bfs(Board(board=[[5, 1, 3], [4, 2, 6], [7, 8, 0]])))))
