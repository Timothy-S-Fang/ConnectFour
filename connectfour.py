import numpy as np

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
    print(np.flip(game_board))
    return

def game_progress():
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):
            if game_board[row][col] == cell_empty:
                continue
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
                continue
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
                continue
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
                continue
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

def get_open_row(col):
    if 0 <= col < COL_SIZE:
        for row in range(ROW_SIZE - 1, -1, -1):
            if game_board[row][col] == cell_empty:
                return row
    return None
                                                       


while not game_over:
    print_board()

    # Player one turn (User)
    if turn == 0:
        col = int(input("Player 1 Choose your move from (0-6)"))
        if 0 <= col < COL_SIZE:  # Check if col is within bounds
            row = get_open_row(col)  
            if row is not None:
                player_turn(game_board, row, col, player_x)
                game_over = game_progress()
            else:
                print('Invalid move')
        else:
            print('Column index out of bounds. Please choose a column between 0 and', COL_SIZE - 1)

    # Player two turn (AI)
    else:
        print("Player 2 (AI) is thinking...")
        col = ai_move(game_board)  # Call the AI function to make a move
        if 0 <= col < COL_SIZE:  # Check if col is within bounds
            row = get_open_row(col)  # Uncomment and place this line here to assign a valid row
            if row is not None:
                player_turn(game_board, row, col, player_y)
                game_over = game_progress()
            else:
                print('AI chose an out-of-bounds column. This is an issue in your AI logic.')

    turn += 1
    turn = turn % 2
