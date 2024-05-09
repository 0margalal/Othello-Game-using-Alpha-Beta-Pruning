from Board import Board
from Player import Player

board = Board()
player1 = Player('human', 'B')
player2 = Player('AI', 'W')

possible_moves = board.getPossibleMoves(player1)
print(possible_moves)
for i in range(8):
    for j in range(8):
        if (i, j) in possible_moves:
            print('X', end=' ')
        else:
            print(board.board[i][j], end=' ')
    print()
