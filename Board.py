from Player import Player
from typing import Self


class Board:
    board = []
    for i in range(8):
        board.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

    def __init__(self):
        self.black = 2
        self.white = 2
        pass

    def isTerminal(self) -> bool:
        return self.black + self.white == 64

    def checkMove(self, i, j, color) -> bool:
        # check if a horizontal move is possible
        for x in range(i + 1, 8):
            if self.board[x][j] == '_':
                break
            elif self.board[x][j] == color and x - i > 1:
                return True
            elif self.board[x][j] == color:
                break
        for x in range(i - 1, -1, -1):
            if self.board[x][j] == '_':
                break
            elif self.board[x][j] == color and i - x > 1:
                return True
            elif self.board[x][j] == color:
                break
        # check if a vertical move is possible
        for y in range(j + 1, 8):
            if self.board[i][y] == '_':
                break
            elif self.board[i][y] == color and y - j > 1:
                return True
            elif self.board[i][y] == color:
                break
        for y in range(j - 1, -1, -1):
            if self.board[i][y] == '_':
                break
            elif self.board[i][y] == color and j - y > 1:
                return True
            elif self.board[i][y] == color:
                break
        # check if a diagonal move is possible
        for x, y in zip(range(i + 1, 8), range(j + 1, 8)):
            if self.board[x][y] == '_':
                break
            elif self.board[x][y] == color and x - i > 1:
                return True
            elif self.board[x][y] == color:
                break
        for x, y in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
            if self.board[x][y] == '_':
                break
            elif self.board[x][y] == color and i - x > 1:
                return True
            elif self.board[x][y] == color:
                break
        for x, y in zip(range(i + 1, 8), range(j - 1, -1, -1)):
            if self.board[x][y] == '_':
                break
            elif self.board[x][y] == color and x - i > 1:
                return True
            elif self.board[x][y] == color:
                break
        for x, y in zip(range(i - 1, -1, -1), range(j + 1, 8)):
            if self.board[x][y] == '_':
                break
            elif self.board[x][y] == color and i - x > 1:
                return True
            elif self.board[x][y] == color:
                break
        return False

    def getPossibleMoves(self, player: Player) -> list[tuple[int, int]]:
        color = player.GetColor()
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == '_':
                    if self.checkMove(i, j, color):
                        possible_moves.append((i, j))
        return possible_moves

    def applyMove(self, player, move) -> Self:
        tempboard = self
        # apply move
        return tempboard

    def makeMove(self, player, move):
        board = self.applyMove(player, move).board

    def displayBoard(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.board)
            print()

    def getWinner(self):
        if self.black > self.white:
            return 'B'
        elif self.white > self.black:
            return 'W'
        return 'D'
