
def create_board():
    # Initialize the board
    return

def player_turn():
    # make a move
    return

def valid_move():
    # returns boolean on whether given spot is available
    return

def print_board():
    # print current game state
    return

def game_progress():
    # check if there is a winning move

    # Horizontal win
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            player = game_board[row][col]
            if game_board[row][col + 1] == player and game_board[row][col + 2] == player and game_board[row][col + 3] == player:
                print("Congratulations! Player " + player + "has won the game on a horizontal connection!")
                game_over = True
    
    # Vertical win
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            player = game_board[row][col]
            if game_board[row][col + 1] == player and game_board[row + 2][col] == player and game_board[row + 3][col] == player:
                print("Congratulations! Player " + player + "has won the game on a horizontal connection!")
                game_over = True
    
    # Positively sloped angles
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            player = game_board[row][col]
            if game_board[row + 1][col + 1] == player and game_board[row + 2][col + 2] == player and game_board[row + 3][col + 3] == player:
                print("Congratulations! Player " + player + "has won the game on a diagonal connection!")
                game_over = True

    # Negatively sloped angles
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            player = game_board[row][col]
            if game_board[row - 1][col + 1] == player and game_board[row - 2][col + 2] == player and game_board[row - 3][col + 3] == player:
                print("Congratulations! Player " + player + "has won the game on a diagonal connection!")
                game_over = True
    return

def game_result():
    # 0 : lose, 1: win, 2: draw
    return

def get_open_row():
    # return the next open row given a column from top down
    return

game_board = create_board()
game_over = False
turn = 0

while not game_over:

    # Player one turn
    if turn == 0:
        col = int(input("Player 1 Choose your move from (0-6)"))
        if valid_move():
            row = get_open_row()
            player_turn(...)
            game_progress()

    # Player two turn
    else:
        col = int(input("Player 2 Choose your move from (0-6)"))
        if valid_move():
            row = get_open_row()
            player_turn(...) 
            game_progress()
    
    print_board()
    turn += 1
    turn = turn % 2