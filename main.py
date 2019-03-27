from board import Board

b = Board()

b.print()
c = b.calculate_child_states()
for x in c:
    x.print()