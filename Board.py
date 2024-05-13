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
        # print(self.black ," and ",self.white)
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
        tempboard = self
        i = int(move[0])
        j = int(move[1])
        tempboard.board[i][j] = player.color
        colorr = player.color

        up = 0
        down = 0
        left = 0
        right = 0
        while i < 7 and tempboard.board[i + 1][j] != '_' and tempboard.board[i + 1][j] != player.color:
            down += 1
            i += 1
        i = move[0]
        if tempboard.board[i][j] == player.color:
            tempboard = tempboard.color_board(i, j, down, 'D', colorr)

        while i >= 1 and tempboard.board[i - 1][j] != '_' and tempboard.board[i - 1][j] != player.color:
            up += 1
            i -= 1
        i = move[0]
        if tempboard.board[i][j] == player.color:
            tempboard = tempboard.color_board(i, j, up, 'U', colorr)

        while j < 7 and tempboard.board[i][j + 1] != '_' and tempboard.board[i][j + 1] != player.color:
            right += 1
            j += 1
        j = move[1]
        if tempboard.board[i][j] == player.color:
            tempboard = tempboard.color_board(i, j, right, 'R', colorr)

        while j >= 1 and tempboard.board[i][j - 1] != '_' and tempboard.board[i][j - 1] != player.color:
            left += 1
            j -= 1
        j = move[1]
        if tempboard.board[i][j] == player.color:
            tempboard = tempboard.color_board(i, j, left, 'L', colorr)

        return tempboard

    def makeMove(self, player, move):
        self.board = self.applyMove(player, move).board
        # return self.applyMove(player, move).board

    def displayBoard(self):
        for element in self.board:
            print(element)
        print()

    def getWinner(self):
        if self.black > self.white:
            return 'B'
        elif self.white > self.black:
            return 'W'
        return 'D'
