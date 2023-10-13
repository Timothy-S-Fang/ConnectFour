import numpy as np
from minimax import minimax, possible_states
import random


ROW_SIZE = 7
COL_SIZE = 6
board_size = (COL_SIZE, ROW_SIZE)
cell_empty = 0
player_x = 1
player_y = 2
game_over = False
turn = 0

game_board = np.zeros(board_size, dtype=int)

def create_board():
    global game_board
    game_board = np.zeros(board_size, dtype=int)

def player_turn(board, row, col, piece):
    board[row][col] = piece

def valid_move(board, col):
    if 0 <= col < COL_SIZE:
        return board[-1][col] == 0
    return False

def print_board():
    print(np.flipud(game_board))

    return

def game_progress():
    # Checks if the game has been won by a certain player and is run every time move is made (check main)

    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                col + 3 < COL_SIZE
                and game_board[row][col + 1] == player
                and game_board[row][col + 2] == player
                and game_board[row][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a horizontal connection!")
                return True

    # Vertical win
    for col in range(COL_SIZE):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                row + 3 < ROW_SIZE
                and game_board[row + 1][col] == player
                and game_board[row + 2][col] == player
                and game_board[row + 3][col] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a vertical connection!")
                return True

    # Positively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                row + 3 < ROW_SIZE
                and col + 3 < COL_SIZE
                and game_board[row + 1][col + 1] == player
                and game_board[row + 2][col + 2] == player
                and game_board[row + 3][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                return True

    # Negatively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(3, ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                row - 3 >= 0
                and col + 3 < COL_SIZE
                and game_board[row - 1][col + 1] == player
                and game_board[row - 2][col + 2] == player
                and game_board[row - 3][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                return True

    return False

def get_open_row(c):
    # return the next open row given a column from top down
   for row in range(ROW_SIZE):
       if game_board[row][c] == cell_empty:
           return row
   return

# def get_open_row(game_board,c):
#     for row in range(ROW_SIZE-2, 0-1,-1):
#         if game_board[row][c] == cell_empty:
#             return row
    # need to set case for when row is filled up

if __name__ == '__main__':
    while not game_over:

        print_board()

        # Player one turn
        if turn == 0:
            col = int(input("Player 1 Choose your move from (0-6)"))
            if valid_move(game_board, col):
                row = get_open_row(col)
                player_turn(game_board, row, col, player_x)
            else:
                print('invalid move')

        # Player two turn
        else:
            col = minimax(game_board, game_over=False, depth = 2, Maximizing=True)[1]
            row = get_open_row(col)
            player_turn(game_board, row, col, player_y)
            print("AI choose to play " + str(col))
        
        game_over = game_progress()
        turn += 1
        turn = turn % 2
        
        # Check for a draw condition (board full)
        if np.all(game_board != cell_empty):
            print("The game is a draw!")
            break
