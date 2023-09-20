import numpy

board_size = (6,7) #size of the columns, rows
cell_empty = 0 #empty cell on board
player_x = 1 #player x piece on board
player_y = 2 #player y piece on board

#define game_board using 2D numpy array
game_board = numpy.zeros(board_size, dtype= int)

def create_board():
    # Initialize the board by uing the 2D numpy array
    global game_board
    game_board = numpy.zeros(board_size, dtype= int)

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

