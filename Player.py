from Board import Board
import math
import copy


def normalizer(value, min, max):
    return (value - min) / (max - min)


def utility(board, player):
    gameStage = board.white + board.black
    if player.color == 'B':
        pieceDifference = board.black - board.white
    else:
        pieceDifference = board.white - board.black
    pieceDifference = normalizer(pieceDifference, 0, 64)
    mobility = len(board.getPossibleMoves(player))
    mobility = normalizer(mobility, 0, 10)
    if gameStage < 12:
        return 6 * mobility
    elif gameStage < 24:
        return 2 * pieceDifference + 4 * mobility
    elif gameStage < 36:
        return 3 * pieceDifference + 3 * mobility
    elif gameStage < 48:
        return 4 * pieceDifference + 2 * mobility
    else:
        return 6 * pieceDifference


class Player:
    def __init__(self, player_type, color):
        self.player_type = player_type
        self.color = color

    def getBestMove(self, depth, possible_moves, initial_board, opp_color):
        P = Player("Human", opp_color)
        best_move = None
        best_score = -1000
        alpha = -math.inf
        beta = math.inf
        bestPossibleMoves = initial_board.getPossibleMoves(self)
        for move in bestPossibleMoves:
            new_board = copy.deepcopy(initial_board)
            new_board = new_board.applyMove(self, move)
            score = self.alpha_beta_minimax(depth - 1, alpha, beta, new_board, False, P.color, P.player_type)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    def alpha_beta_minimax(self, depth, alpha, beta, board, robot, opp_color, opp_pt):
        if robot:
            max_eval = -1000
            legal_moves = board.getPossibleMoves(self)
            if depth == 0 or board.isTerminal() or len(legal_moves) == 0:
                return utility(board, self)
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = new_board.applyMove(self, move)
                eval = self.alpha_beta_minimax(depth - 1, alpha, beta, new_board, False, opp_color, opp_pt)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 1000
            legal_moves = board.getPossibleMoves(Player(opp_pt, opp_color))
            if depth == 0 or board.isTerminal() or len(legal_moves) == 0:
                return utility(board, Player(opp_pt, opp_color))
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = new_board.applyMove(Player(opp_pt, opp_color), move)
                eval = self.alpha_beta_minimax(depth - 1, alpha, beta, new_board, True, opp_color, opp_pt)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def getColor(self):
        return self.color
