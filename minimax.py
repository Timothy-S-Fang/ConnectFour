import numpy as np
import unittest

# Constants for player representation
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = 2
ROW_SIZE = 6
COL_SIZE = 7
board_size = (COL_SIZE,ROW_SIZE) #size of the columns, rows
cell_empty = 0 #empty cell on board
player_x = 1 #player x piece on board
player_y = 2 #player y piece on board


def evaluate_position(board):
    """An evaluation function that assigns a score to the board state
    by adding the possible score for all directions.
    Returns the score."""
    score = 0
    # Horizontal Evaluation
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):
            horizontal_pieces = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            contains_AI = horizontal_pieces.count(AI_PLAYER)
            contains_Player = horizontal_pieces.count(HUMAN_PLAYER)

            if contains_AI > 0 and contains_Player == 0:
                score += 1
            elif contains_Player > 0 and contains_AI == 0:
                score -= 1
        
    # Vertical win
    for col in range(COL_SIZE):
        for row in range(ROW_SIZE - 3):
            vertical_pieces = [board[row][col], board[row + 1][col], board[row + 2][col], board[row + 3][col]]
            contains_AI = vertical_pieces.count(AI_PLAYER)
            contains_Player = vertical_pieces.count(HUMAN_PLAYER)
            if contains_AI > 0 and contains_Player == 0:
                score += 1
            elif contains_Player > 0 and contains_AI == 0:
                score -= 1
    
    # Positively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE - 3):
            pos_slope_pieces = [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2], board[row + 3][col + 3]]
            contains_AI = pos_slope_pieces.count(AI_PLAYER)
            contains_Player = pos_slope_pieces.count(HUMAN_PLAYER)

            if contains_AI > 0 and contains_Player == 0:
                score += 1
            elif contains_Player > 0 and contains_AI == 0:
                score -= 1
    
    # Negatively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(3, ROW_SIZE):
            neg_slope_piece = [board[row][col], board[row - 1][col + 1], board[row - 2][col + 2], board[row - 3][col + 3]]
            contains_AI = neg_slope_piece.count(AI_PLAYER)
            contains_Player = neg_slope_piece.count(HUMAN_PLAYER)

            if contains_AI > 0 and contains_Player == 0:
                score += 1
            elif contains_Player > 0 and contains_AI == 0:
                score -= 1
                
    return score

def player_turn(board, row, col, piece):
    """A function allowing the AI-player to make a move."""
    board[row][col] = piece

def get_legal_moves(board):
    """Gets the legal next moves,
    it returns a list of the first open row for each column."""
    legal_moves = []
    for col in range(COL_SIZE):
        if board[-1][col] == 0:
            legal_moves.append(col)
    return legal_moves


def get_open_row(board,col):
    """Returns the next open row from top down, given the column"""
    for row in range(ROW_SIZE):
       if board[row][col] == cell_empty:
           return row
    return

def winning_move(board, piece):
    """A funciton checking if a winning move is being made.
    Returns True if that is the case."""
	# Check horizontal locations for win
    for c in range(COL_SIZE-3):
        for r in range(ROW_SIZE):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

	# Check vertical locations for win
    for c in range(COL_SIZE):
        for r in range(ROW_SIZE-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

	# Check positively sloped diagonals
    for c in range(COL_SIZE-3):
    	for r in range(ROW_SIZE-3):
	    	if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
	    		return True

    # Check negatively sloped diagonals
    for c in range(COL_SIZE-3):
        for r in range(3, ROW_SIZE):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def minimax(game_board, depth, alpha, beta, Maximizing=True):
    """A function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning
    Returns the score and best move."""
    # run minimax until the depth reaches 0
    # check for win/score
    if depth == 0:
        if winning_move(game_board, AI_PLAYER):
            return (100000000000000, None)
        elif winning_move(game_board, HUMAN_PLAYER):
            return (-10000000000000, None)
        return (evaluate_position(game_board), None)
    
    possible_cols = get_legal_moves(game_board) # possible next moves
    best_move = 0 # 0-6 move for AI (initial starting value)

    if Maximizing:
        value = float('-inf') # score is set to negative infinity

        # get the score for each possible next move, save the best one
        # and the move associated with it
        # (go into each branch of the tree, interrupt by pruning
        # if it leads to a state that is in the advantage of opposite
        # player)
        for col in possible_cols:
            row = get_open_row(game_board, col)
            temp_board = game_board.copy()
            player_turn(temp_board, row, col, AI_PLAYER) 
            new_value= minimax(temp_board, depth - 1, alpha, beta, False)[0]
            if new_value > value: # update score and best_move
                value = new_value
                best_move = col
            alpha = max(alpha, value) # update alpha
            if beta <= alpha: #prune the tree
                break


        return value, best_move
    
    # the minimising player
    else:
        value = float('+inf') # score is set to positive infinity

        for col in possible_cols:
            row = get_open_row(game_board, col)
            temp_board = game_board.copy()
            player_turn(temp_board, row, col, HUMAN_PLAYER) 
            new_value = minimax(temp_board, depth - 1, alpha, beta, True)[0]
            if new_value < value: # update score and best_move
                value = new_value
                best_move = col
            beta = min(beta,value) # update beta
            if beta <= alpha: # prune the tree
                break
                
        return value, best_move


class TestMinimax(unittest.TestCase):
    def test_evaluate_position(self):
        game_board = np.zeros((6, 7), dtype=int)
        score = evaluate_position(game_board)
        self.assertEqual(score, 0)  # Ensure the initial score is as expected

    def test_minimax(self):
        game_board = np.zeros((6, 7), dtype=int)
        depth = 4
        alpha = float('-inf')
        beta = float('inf')
        maximizing = True
        score, best_move = minimax(game_board, depth, alpha, beta, maximizing)
        self.assertIsInstance(score, int)  # Ensure the score is an integer
        self.assertIsInstance(best_move, int)  # Ensure the best_move is an integer

if __name__ == '__main__':
    unittest.main()
    

