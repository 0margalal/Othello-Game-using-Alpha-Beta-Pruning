from Board import Board
import math


class Player:
    def __init__(self, player_type, color):
        self.player_type = player_type
        self.color = color

    def getBestMove( self, depth, possible_moves, initial_board , opp_color ):
        P = Player("Human","opp_color")
        best_move = None
        best_score = -1000
        new_board = Board()
        alpha=-math.inf
        beta=math.inf
        robot=False
        for move in initial_board.getPossibleMoves( self):
            new_board = initial_board.applyMove(self,move)
            score = self.alpha_beta_minimax( depth, alpha , beta , new_board , robot , P.color , P.player_type)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move
    def alpha_beta_minimax(self, depth, alpha, beta, board , robot , opp_color , opp_pt):
        if depth == 0:
            return (board.white - board.black)
        legal_moves = board.getPossibleMoves(self)
        if not robot:
            legal_moves = board.getPossibleMoves(Player(opp_pt,opp_color))
        if len(legal_moves) == 0:
            return (board.white-board.black)

        if robot:
            max_eval = -1000
            new_board = Board()
            for move in legal_moves:
                new_board = board.applyMove( self, move)
                eval = self.alpha_beta_minimax( depth-1 ,alpha, beta, new_board, False , opp_color , opp_pt)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 1000
            new_board = Board()
            oppenent = Player(opp_pt,opp_color)
            for move in legal_moves:
                new_board= board.applyMove( oppenent,move) #ADD THE OTHER PLAYER
                eval = self.alpha_beta_minimax( depth-1 ,alpha, beta, new_board, True , opp_color , opp_pt)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def getColor(self):
        return self.color
