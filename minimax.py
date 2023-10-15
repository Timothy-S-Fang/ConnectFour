import numpy as np


# Constants for player representation
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = 2
ROW_SIZE = 6
COL_SIZE = 7


def evaluate_position(board):
    # Implement an evaluation function that assigns a score to the board state
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
    board[row][col] = piece

def minimax(state, game_board, depth, alpha, beta, maximizing=True):
    if depth == 0:
        return evaluate_position(game_board)

    if maximizing:
        best_value = -float('inf')
        for child in possible_states(state, game_board, AI_PLAYER):
            value = minimax(state, child, depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha,value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('inf')
        for child in possible_states(state, game_board, HUMAN_PLAYER):
            value = minimax(state, child, depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_value

def game_is_over(board):
    # Implement a function to check if the game is over (e.g., someone has won or it's a draw).
    pass

def get_legal_moves(board):
    # Implement a function to return a list of legal moves (e.g., available columns to drop a piece).
    legal_moves = []
    for col in range(COL_SIZE):
        if board[-1][col] == 0:
            legal_moves.append(col)
    return legal_moves

def make_move(board, row, col, player):
    # Implement a function to make a move on the board.
    pass

def undo_move(board, row, col):
    # Implement a function to undo a move on the board.
    pass

board_size = (COL_SIZE,ROW_SIZE) #size of the columns, rows
cell_empty = 0 #empty cell on board
player_x = 1 #player x piece on board
player_y = 2 #player y piece on board
game_over = False
turn = 0

#define game_board using 2D np array
#game_board = np.zeros(board_size, dtype= int)


def get_open_row(game_board,c):
    for row in range(ROW_SIZE):
       if game_board[row][c] == cell_empty:
           return row
    return

def possible_states(game_board, piece):
    new_states = []

    for col in range(ROW_SIZE):
        open_row = get_open_row(game_board,col)
        game_board_copy = game_board.copy()
        game_board_copy[open_row][col] = piece
        new_states.append(game_board_copy)
    return new_states

def winning_move(board, piece):
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

	# Check positively sloped diaganols
	for c in range(COL_SIZE-3):
		for r in range(ROW_SIZE-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COL_SIZE-3):
		for r in range(3, ROW_SIZE):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def minimax(game_board,game_over, depth, alpha, beta, Maximizing=True):
    """a function going through the tree and picking
    the best possible move in a game. Also implementing AlphaBeta pruning"""
    # Maybe setting a depth limit as well????

    if game_over != True:

        if depth == 0:
            if winning_move(game_board, AI_PLAYER):
                return (100000000000000, None)
            elif winning_move(game_board, HUMAN_PLAYER):
                return (-10000000000000, None)
            return (evaluate_position(game_board), None)
        
        possible_cols = get_legal_moves(game_board)
        best_move = 0 # 0-6 move for AI (initial starting value)

        if Maximizing:
            value = float('-inf')

            for col in possible_cols:
                row = get_open_row(game_board, col)
                temp_board = game_board.copy()
                player_turn(temp_board, row, col, AI_PLAYER) 
                new_value= minimax(temp_board,game_over, depth - 1, alpha, beta, False)[0]
                if new_value > value:
                    value = new_value
                    best_move = col
                alpha = max(alpha, value)
                if beta <= alpha:
                    break


            return value, best_move
        
        else:
            value = float('+inf')

            for col in possible_cols:
                row = get_open_row(game_board, col)
                temp_board = game_board.copy()
                player_turn(temp_board, row, col, HUMAN_PLAYER) 
                new_value = minimax(temp_board,game_over, depth - 1, alpha, beta, True)[0]
                if new_value < value:
                    value = new_value
                    best_move = col
                beta = min(beta,value)
                if beta <= alpha:
                    break
                    
            return value, best_move


# if __name__ == "__main__":
#     game_board[5][2] = 1
#     game_board[5][5] = 1
#     game_board[5][4] = 2
#     states = possible_states(game_board,2)
#     for state in states:
#         #print(state)
#         ids =[minimax(state, game_over=False, depth = 5, Maximizing=True) for state in states]
#     game_board = states[max(ids)]

