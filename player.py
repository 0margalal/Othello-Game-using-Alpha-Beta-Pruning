class Player:
    def __init__(self, player_type, color):
        self.player_type = player_type
        self.color = color

    def getBestMove(self, board, depth):
        pass
    # Implement Alpha-Beta Pruning minimax

    def MaxValue(self, board, alpha, beta, depth) -> float:
        pass

    def MinValue(self, board, alpha, beta, depth) :
        pass

    def utility(self, board):
        pass
