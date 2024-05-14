from Board import Board
from Player import Player
import pygame
import copy
import math
import time
import sys


board = Board()

pygame.init()

WIDTH, HEIGHT = 600, 700
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
COUNTER_HEIGHT = 100

GREEN = (8, 148, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)


def draw_Board(screen, possible_moves):
    screen.fill(GREEN)

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, COUNTER_HEIGHT + y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if board.board[x][y] == 'B':
                pygame.draw.circle(screen, BLACK,
                                   (x * CELL_SIZE + CELL_SIZE // 2, COUNTER_HEIGHT + y * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 2)

            elif board.board[x][y] == 'W':
                pygame.draw.circle(screen, WHITE,
                                   (x * CELL_SIZE + CELL_SIZE // 2, COUNTER_HEIGHT + y * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 2)
            elif (x, y) in possible_moves:
                pygame.draw.circle(screen, GRAY,
                                   (x * CELL_SIZE + CELL_SIZE // 2, COUNTER_HEIGHT + y * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 2, 3)


def count_pieces():
    board.black = sum(row.count('B') for row in board.board)
    board.white = sum(row.count('W') for row in board.board)


def init_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Othello")
    return screen


def main():
    turn = 1  # 1 for black, 2 for white
    screen = init_screen()
    players = [Player('Human', 'B')]
    playerType = input('Choose White player type (Human/AI): ')
    while playerType not in ['Human', 'AI']:
        playerType = input('Choose White player type (Human/AI): ')
    players.append(Player(playerType, 'W'))
    depth = 0
    if players[0].player_type == 'AI' or players[1].player_type == 'AI':
        depth = int(input('Choose difficulty ( 1 -> Easy / 3 -> Medium / 5 -> Hard ) : '))
        while depth not in [1, 3, 5]:
            depth = int(input('Difficulty must be either ( 1 -> Easy / 3 -> Medium / 5 -> Hard ) : '))
    depth *= 2


    print('\nGame Start\n')
    font = pygame.font.SysFont(None, 36)
    font2 = pygame.font.SysFont(None, 60)
    flag = False
    while not board.isTerminal():
        count_pieces()
        player = players[turn - 1]
        possible_moves = board.getPossibleMoves(player)
        if len(possible_moves) == 0:
            turn = 3 - turn
            player = players[turn - 1]
            possible_moves1 = board.getPossibleMoves(player)
            if len(possible_moves1) == 0:
                turn = 3 - turn
                flag = True
                break

        if player.player_type == 'Human':
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // CELL_SIZE, (pos[1] - COUNTER_HEIGHT) // CELL_SIZE
                    if (x, y) in possible_moves:
                        move = (x, y)
                        turn = 3 - turn
                        board.makeMove(player, move)
                    else:
                        continue
        else:
            time.sleep(0.5)
            new_board = copy.deepcopy(board)
            move = player.getBestMove( depth , possible_moves, new_board , players[(turn+1)%2].color)
            board.makeMove(player, move)
            turn = 3 - turn
        draw_Board(screen, possible_moves)

        count_pieces()
        black_text = font.render(f" White: {board.white}", True, WHITE)
        screen.blit(black_text, (WIDTH - 150, 20))

        white_text = font.render(f" Black: {board.black}", True, BLACK)
        screen.blit(white_text, (20, 20))

        turn_text = font.render("Turn:", True, BLACK)
        player_text = font.render("Black" if (turn == 1) else "White", True, BLACK)
        screen.blit(turn_text, (WIDTH // 2 - 80, 20))
        screen.blit(player_text, (WIDTH // 2 - 20, 20))

        pygame.display.update()
    pygame.display.update()

    winner = board.getWinner()

    game_over = font2.render("Game Over:", True, RED)
    text_width_game_over, text_height_game_over = game_over.get_size()
    screen.blit(game_over, (WIDTH // 2 - text_width_game_over // 2, 310))
    if flag==True:
        deadend = font2.render("Because of Deadend:", True, RED)
        text_width_deadend, text_height_deadend = deadend.get_size()
        screen.blit(deadend, (WIDTH // 2 - text_width_deadend // 2, 350))

    print_winner = font2.render("BLACK WINS!" if winner == 'B' else "WHITE WINS!" if winner == 'W' else "Draw!", True,
                               RED)
    text_width_winner, text_height_winner = print_winner.get_size()
    screen.blit(print_winner, (WIDTH // 2 - text_width_winner // 2, 390))

    pygame.display.update()

    print('\nGame Over\n')
    if winner == 'B':
        print('Black wins!')
    elif winner == 'W':
        print('White wins!')
    else:
        print('Draw!')
    x = input()


if __name__ == '__main__':
    main()
