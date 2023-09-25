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
    new_states = []
    for col in range(state-1,state+2):
        if col <= COL_SIZE:
            print(col)
            space = np.flatnonzero(np.flip(game_board[:, col]))
            if space.size > 0:
                space = space[0]
            new_states.append(space)
    return new_states



def minimax(state,game_board,game_over, Maximizing=True):
    """a function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning"""
    #Maybe setting a depth limit as well????
    if game_over != True:
        if Maximizing:
            value = float('-inf')
            next_states = possible_states(state, game_board)
            for child in next_states:
                value = max(value, minimax(child,game_board,game_over,False))
            return value
        else:
            value = float('+inf')
            next_states = possible_states(state, game_board)
            for child in next_states:
                value = min(value, minimax(child,game_board,game_over,True))
            return value


if __name__ == "__main__":
    game_board[3][2] = 1
    game_board[5][5] = 1
    possible_states(6, game_board)