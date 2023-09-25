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

def possible_states(state, game_board):
    for col in range(game_board.shape[1]):
        print("col",np.flatnonzero(np.flip(game_board[:, col])))


def minimax(state,game_board,game_over, Maximizing=True):
    """a function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning"""
    #Maybe setting a depth limit as well????
    if game_over != True:
        possible_states = ()

if __name__ == "__main__":
    game_board[3][2] = 1
    possible_states(2, game_board)