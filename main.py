from Board import Board
from Player import Player


def main():
    board = Board()

    players = []
    playerType = input('Choose Black player type (human/AI): ')
    players.append(Player(playerType, 'B'))
    playerType = input('Choose White player type (human/AI): ')
    players.append(Player(playerType, 'W'))

    depth = int(input('Choose search depth: '))
    while depth < 1:
        depth = int(input('Depth must be greater than 0. Choose search depth: '))
    while depth > 6:
        depth = int(input('Depth must be less than 7. Choose search depth: '))

    print('Game Start')

    count = 0

    while not board.isTerminal():
        board.displayBoard()
        player = players[count % 2]
        possible_moves = board.getPossibleMoves(player)
        print('Possible moves: ', possible_moves)
        if len(possible_moves) == 0:
            print('No possible moves. Turn skipped.')
            count += 1
            continue
        if player.player_type == 'human':
            move = input('Enter move: ').split()
            move = (int(move[0]), int(move[1]))
            while move not in possible_moves:
                move = input('Invalid move. Enter move: ').split()
                move = (int(move[0]), int(move[1]))
            board.makeMove(player, move)
        else:
            move = player.getBestMove(board, possible_moves, depth)
            board.makeMove(player, move)
        count += 1

    print('Game Over')
    winner = board.getWinner()
    if winner == 'B':
        print('Black wins')
    elif winner == 'W':
        print('White wins')
    else:
        print('Draw')


if __name__ == '__main__':
    main()