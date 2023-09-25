import numpy as np

ROW_SIZE = 7
COL_SIZE = 6
board_size = (COL_SIZE,ROW_SIZE) #size of the columns, rows
cell_empty = 0 #empty cell on board
player_x = 1 #player x piece on board
player_y = 2 #player y piece on board
game_over = False
turn = 0

#define game_board using 2D np array
game_board = np.zeros(board_size, dtype= int)

def create_board():
    # Initialize the board by uing the 2D np array
    global game_board
    game_board = np.zeros(board_size, dtype= int)

def player_turn(board, row, col, piece):
    # make a move
    board[row][col] = piece

def valid_move(board, col):
    # returns boolean on whether given spot is available
    if col > 6 or col < 0:
        return False
    return board[-1][col] == 0

def print_board():
    # print current game state
    print(np.flip(game_board))
    return

def game_progress():
    # check if there is a winning move and return value of game_over

    # Horizontal win
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break 
            player = game_board[row][col]
            if game_board[row][col + 1] == player and game_board[row][col + 2] == player and game_board[row][col + 3] == player:
                print("Congratulations! Player " + str(player) + " has won the game on a horizontal connection!")
                return True
    
    # Vertical win
    for col in range(COL_SIZE):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break  
            player = game_board[row][col]
            if game_board[row + 1][col] == player and game_board[row + 2][col] == player and game_board[row + 3][col] == player:
                print("Congratulations! Player " + str(player) + " has won the game on a vertical connection!")
                return True
    
    # Positively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break  
            player = game_board[row][col]
            if game_board[row + 1][col + 1] == player and game_board[row + 2][col + 2] == player and game_board[row + 3][col + 3] == player:
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                return True

    # Negatively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(3, ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break  
            player = game_board[row][col]
            if game_board[row - 1][col + 1] == player and game_board[row - 2][col + 2] == player and game_board[row - 3][col + 3] == player:
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                return True
    return False

def get_open_row(c):
    # return the next open row given a column from top down
    for row in range(ROW_SIZE):
        if game_board[row][c] == cell_empty:
            return row

    return

while not game_over:
    print_board()
    # Player one turn
    if turn == 0:
        col = int(input("Player 1 Choose your move from (0-6)"))
        if valid_move(game_board, col):
            row = get_open_row(col)
            player_turn(game_board, row, col, player_x)
            game_over = game_progress()
        else:
            print('invalid move')

    # Player two turn
    else:
        col = int(input("Player 2 Choose your move from (0-6)"))
        if valid_move(game_board, col):
            row = get_open_row(col)
            player_turn(game_board, row, col, player_y) 
            game_over = game_progress()
        else:
            print('invalid move')

    
    turn += 1
    turn = turn % 2