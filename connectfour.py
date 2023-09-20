
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

def winning_move():
    # check if there is a winning move
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

    # Player two turn
    else:
        col = int(input("Player 2 Choose your move from (0-6)"))
        if valid_move():
            row = get_open_row()
            player_turn(...)

            if ():
                print("Congratulations, Player 2 wins!")
                game_over = True
    
    print_board()
    turn += 1
    turn = turn % 2