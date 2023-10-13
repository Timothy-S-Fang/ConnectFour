import numpy as np

#from connectfour import get_open_row, player_turn
# Constants for player representation
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = 2
ROW_SIZE = 7
COL_SIZE = 6


def evaluate_position(board):
    # Implement an evaluation function that assigns a score to the board state
    score = 0

    # Horizontal Evaluation
    for col in range(COL_SIZE - 3):

        for row in range(ROW_SIZE-1):

            horizontal_pieces = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            contains_AI = horizontal_pieces.count(AI_PLAYER)
            contains_Player = horizontal_pieces.count(HUMAN_PLAYER)

            if contains_AI > 0 and contains_Player == 0:
                score += 1
            elif contains_Player > 0 and contains_AI == 0:
                score -= 1
            
    return score


def minimax(state, game_board, depth, maximizing=True):
    if depth == 0 or game_progress(game_board):
        return evaluate_position(game_board)

    if maximizing:
        best_value = -float('inf')
        for child in possible_states(state, game_board, AI_PLAYER):
            value = minimax(state, child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in possible_states(state, game_board, HUMAN_PLAYER):
            value = minimax(state, child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value

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
#game_board = np.zeros(board_size, dtype= int)


def new_get_open_row(game_board,c):
    for row in range(ROW_SIZE-2, 0-1,-1):
        if game_board[row][c] == cell_empty:
            return row

def possible_states(game_board, piece):
    new_states = []

    for col in range(ROW_SIZE):
        open_row = new_get_open_row(game_board,col)
        #print(open_row)
        game_board_copy = np.flip(game_board.copy())
        #print(game_board_copy)
        game_board_copy[open_row][col] = piece
        new_states.append(game_board_copy)
    return new_states


def minimax(game_board,game_over, depth, Maximizing=True):
    """a function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning"""
    #Maybe setting a depth limit as well????

    if game_over != True:

        if depth == 0:
            return evaluate_position(game_board)
        
        if Maximizing:
            value = float('-inf')
            next_states = possible_states(game_board, 2)
            for child_state in next_states:
                value = max(value, minimax(child_state,game_over, depth - 1, False))
            return value
        else:
            value = float('+inf')
            next_states = possible_states(game_board, 1)
            for child_state in next_states:
                value = min(value, minimax(child_state,game_over, depth - 1, True))
            return value


if __name__ == "__main__":
    game_board[5][2] = 1
    game_board[5][5] = 1
    game_board[5][4] = 2
    print(game_board)
    states = possible_states(game_board,2)
    for state in states:
        #print(state)
        ids =[minimax(state, game_over=False, depth = 5, Maximizing=True) for state in states]
    game_board = states[max(ids)]
    print(game_board)

