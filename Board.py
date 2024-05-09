class Board:
    board = ['_' * 8] * 8
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

    def __init__(self):
        self.black = 2
        self.white = 2
        pass

    def getPossibleMoves(self, player) -> list[tuple[int, int]]:
        possible_moves = []
        # [[2,4], [3,5], [4,6]]
        pass

    def applyMove(self, player, move) -> list[str]:
        tempboard = self.board
        # apply move
        return tempboard

    def makeMove(self, player, move):
        board = self.applyMove(player, move)
