import numpy as np

# Constants for player representation
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = 2

def evaluate_position(board):
    # Implement an evaluation function to assign a score to the board state.
    # Consider factors like the number of pieces in a row, positional advantages, etc.
    # Positive scores are good for the AI, and negative scores are good for the opponent.
    # Return a higher score for better positions.
    pass

def game_is_over(board):
    # Implement a function to check if the game is over (e.g., someone has won or it's a draw).
    pass

def get_legal_moves(board):
    # Implement a function to return a list of legal moves (e.g., available columns to drop a piece).
    pass

def make_move(board, row, col, player):
    # Implement a function to make a move on the board.
    pass

def undo_move(board, row, col):
    # Implement a function to undo a move on the board.
    pass

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
