from typing import Self
import copy


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
        return False

    def getPossibleMoves(self, player) -> list[tuple[int, int]]:
        color = player.color
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == '_':
                    if self.checkMove(i, j, color):
                        possible_moves.append((i, j))
        return possible_moves

    def color_board(self, i, j, count, direction, colorr):
        while count:
            k = 0
            if direction == 'R':
                k = 1
                j += k

            if direction == 'L':
                k = -1
                j += k

            if direction == 'U':
                k = -1
                i += k

            if direction == 'D':
                k = +1
                i += k
            self.board[i][j] = colorr
            count -= 1
        return self

    def applyMove(self, player, move) -> Self:
        i = int(move[0])
        j = int(move[1])
        tempboard = copy.deepcopy(self)
        if (move == None):
            return tempboard
        tempboard.board[i][j] = player.color
        colorr = player.color
        for x in range(i + 1, 8):
            if tempboard.board[x][j] == '_':
                break
            elif tempboard.board[x][j] == player.color and x - i > 1:
                tempboard = tempboard.color_board(i, j, x - i - 1, 'D', colorr)
                break
            elif tempboard.board[x][j] == player.color:
                break
        for x in range(i - 1, -1, -1):
            if tempboard.board[x][j] == '_':
                break
            elif tempboard.board[x][j] == player.color and i - x > 1:
                tempboard = tempboard.color_board(i, j, i - x - 1, 'U', colorr)
                break
            elif tempboard.board[x][j] == player.color:
                break
        for y in range(j + 1, 8):
            if tempboard.board[i][y] == '_':
                break
            elif tempboard.board[i][y] == player.color and y - j > 1:
                tempboard = tempboard.color_board(i, j, y - j - 1, 'R', colorr)
                break
            elif tempboard.board[i][y] == player.color:
                break
        for y in range(j - 1, -1, -1):
            if tempboard.board[i][y] == '_':
                break
            elif tempboard.board[i][y] == player.color and j - y > 1:
                tempboard = tempboard.color_board(i, j, j - y - 1, 'L', colorr)
                break
            elif tempboard.board[i][y] == player.color:
                break
        tempboard.black = sum(row.count('B') for row in tempboard.board)
        tempboard.white = sum(row.count('W') for row in tempboard.board)
        return tempboard

    def makeMove(self, player, move):
        self.board = self.applyMove(player, move).board
        # return self.applyMove(player, move).board

    def displayBoard(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=' ')
        print()

    def getWinner(self):
        if self.black > self.white:
            return 'B'
        elif self.white > self.black:
            return 'W'
        return 'D'
