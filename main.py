from Board import Board
from Player import Player


def main():
    board = Board()

    players = []
    playerType = input('Choose Black player type (Human/AI): ')
    while playerType not in ['Human','AI']:
        playerType = input('Choose Black player type (Human/AI): ')
    players.append(Player(playerType, 'B'))
    playerType = input('Choose White player type (Human/AI): ')
    while playerType not in ['Human','AI']:
        playerType = input('Choose Black player type (Human/AI): ')
    players.append(Player(playerType, 'W'))

    depth = int(input('Choose difficulty ( 1 -> Easy / 3 -> Medium / 5 -> Hard ) : '))
    while depth not in [1, 3, 5]:
        depth = int(input('Difficulty must be either ( 1 -> Easy / 3 -> Medium / 5 -> Hard ) : '))

    print('\nGame Start\n')
    board.displayBoard()

    count = 0

    while not board.isTerminal():
        print('\n')
        player = players[count % 2]
        print("White's Turn\n" if count % 2 else "Black's Turn\n")
        possible_moves = board.getPossibleMoves(player)
        if len(possible_moves) == 0:
            print('No possible moves. Turn skipped.')
            count += 1
            continue
        print('Possible moves: ', possible_moves)
        if player.player_type == 'Human':
            move = input('Enter move: ').split()
            move = (int(move[0]), int(move[1]))
            while move not in possible_moves:
                move = input('Invalid move. Enter move: ').split()
                print('Possible moves: ', possible_moves)
                move = (int(move[0]), int(move[1]))
            board.makeMove(player, move)
        else:
            move = player.getBestMove(board, possible_moves, depth)
            board.makeMove(player, move)
        count += 1

    print('\nGame Over\n')
    winner = board.getWinner()
    if winner == 'B':
        print('Black wins!')
    elif winner == 'W':
        print('White wins!')
    else:
        print('Draw!')


if __name__ == '__main__':
    main()
