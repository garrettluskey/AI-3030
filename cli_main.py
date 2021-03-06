from timeit import default_timer as timer
from board import Board
from searches import a_star_search, greedy_search, bfs, bfs2
from os import linesep


class CLI:
    help_str = linesep.join(["q: quit", "b: print board", "g: print goal state", "scb: scramble board",
                             "cb: create your own board", "sob: solve board", "sbs: solve board with steps",
                             "sa: print solve algorithm", "ssaas: set solve algorithm to A Star",
                             "ssag: set solve algorithm to Greedy", "ssabfs: set solve algorithm to BFS"])
    a_star_id = 'A Star'
    greedy_id = 'Greedy'
    breadth_first_id = 'Breadth First'
    current_solver_id = a_star_id

    def __init__(self):
        self.board = Board()

    def main(self):
        command = 'h'
        while command != 'q':
            if command == 'b':
                print(self.board)
            elif command == 'g':
                print(Board())
            elif command == 'scb':
                self.board.scramble()
                command = 'b'
                continue
            elif command == 'cb':
                self.construct_board()
                print("The current board is:")
                command = 'b'
                continue
            elif command == 'sob':
                self.solve()
            elif command == 'sbs':
                self.solve(with_steps=True)
            elif command == 'sa':
                print(self.current_solver_id)
            elif command == 'ssaas':
                self.current_solver_id = self.a_star_id
                print("solver algorithm set to:")
                command = 'sa'
                continue
            elif command == 'ssag':
                self.current_solver_id = self.greedy_id
                print("solver algorithm set to:")
                command = 'sa'
                continue
            elif command == 'ssabfs':
                self.current_solver_id = self.breadth_first_id
                print("solver algorithm set to:")
                command = 'sa'
                continue
            elif command == 'h':
                print(self.help_str)
            else:
                print("Error: Unknown command")
                command = 'h'
                continue
            command = input()

    def construct_board(self):
        print("Type the board digits from one row at a time left to right starting with the top row. (0 represents "
              "blank)")
        print("Example: 123456780 would represent the goal board")
        input_string = input()
        if len(input_string) != 9:
            print("The string wasn't 9 digit's long")
            return
        board = Board()
        i = 0
        for y in range(board.get_board_height()):
            for x in range(board.get_board_width()):
                if not input_string[i].isdigit():
                    print("One of the characters wasn't a digit")
                board.board[y][x] = int(input_string[i])
                i += 1
        try:
            board = Board(board.get_current_state())
        except ValueError as ve:
            print(ve)
            return
        self.board = board

    def solve(self, with_steps=False):
        print("Solving with {0}".format(self.current_solver_id))
        if self.current_solver_id == self.a_star_id:
            solver = a_star_search
        elif self.current_solver_id == self.greedy_id:
            solver = greedy_search
        elif self.current_solver_id == self.breadth_first_id:
            solver = bfs2
        else:
            return
        start = timer()
        steps = solver(self.board)
        time = timer() - start
        print("Done in {0} seconds".format(time))
        print("Move count: {0}".format(len(steps)))
        print("Listing steps:")
        for i in range(len(steps)):
            print("step {0}:".format(i))
            print(steps[i])


if __name__ == '__main__':
    print("Starting 8 puzzle solver CLI...")
    CLI().main()
