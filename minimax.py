import numpy as np

# Constants for player representation
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = 2
ROW_SIZE = 7
COL_SIZE = 6

from connectfour import get_open_row, player_turn



def evaluate_position(board):
    # Implement an evaluation function to assign a score to the board state.
    # Consider factors like the number of pieces in a row, positional advantages, etc.
    # Positive scores are good for the AI, and negative scores are good for the opponent.
    # Return a higher score for better positions.

    score = 0

    # Horizontal Evaluation

    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):

            horizontal_pieces = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            contains_AI = False
            contains_Player = False

            for h in horizontal_pieces:
                if h == HUMAN_PLAYER:
                    contains_Player = True
                if h == AI_PLAYER:
                    contains_AI = True
            
            if contains_AI and not contains_Player:
                # has at least 1 AI piece and no player pieces
                score += 1
            elif contains_Player and not contains_AI:
                # has at least 1 player piece and no AI pieces
                score -= 1
            
    return score

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

def possible_states(state, game_board, piece):
    new_states = []
    for col in range(ROW_SIZE):
        open_row = get_open_row(col)
        game_board_copy = game_board
        player_turn(game_board_copy, open_row, col, piece)
        new_states.append(game_board_copy)
    return new_states



def minimax(state,game_board,game_over, depth, Maximizing=True):
    """a function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning"""
    #Maybe setting a depth limit as well????

    if game_over != True:

        if depth == 0:
            return evaluate_position(game_board)
        
        if Maximizing:
            value = float('-inf')
            next_states = possible_states(state, game_board)
            for child in next_states:
                value = max(value, minimax(child,game_board,game_over, depth - 1, False))
            return value
        else:
            value = float('+inf')
            next_states = possible_states(state, game_board)
            for child in next_states:
                value = min(value, minimax(child,game_board,game_over, depth - 1, True))
            return value


if __name__ == "__main__":
    game_board[3][2] = 1
    game_board[5][5] = 1
    possible_states(6, game_board)
