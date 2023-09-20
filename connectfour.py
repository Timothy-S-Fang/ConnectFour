
def create_board():
    # Initialize the board
    return

def player_turn(board,row, col, piece):
    # make a move
    board[row][col] = piece

def valid_move(board, col):
    # returns boolean on whether given spot is available
    return board[-1][col] == 0

def print_board():
    # print current game state
    print(np.flip(board))

def game_result():
    # 0 : lose, 1: win, 2: draw
    return

