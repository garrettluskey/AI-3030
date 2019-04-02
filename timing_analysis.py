from searches import a_star_search, greedy_search, bfs, bfs2
from board import Board
from timeit import default_timer as timer
import asyncio


boards = []
for i in range(10):
    board = Board()
    board.scramble()
    boards.append(board)

def solve(solver, board):
    start = timer()
    steps = solver(board)
    time = timer()-start
    print("Done in {0} seconds".format(time))
    print("Move count: {0}".format(len(steps)))

for board in boards:
    for solver in [a_star_search, greedy_search, bfs]:
        solve(solver, board)


