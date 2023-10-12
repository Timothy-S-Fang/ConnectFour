import numpy as np
from connectfour import ROW_SIZE, COL_SIZE, AI_PLAYER, HUMAN_PLAYER, game_board, valid_move, get_open_row, game_progress

# Constants for player representation
EMPTY = 0

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

def possible_states(state, game_board, piece):
    new_states = []
    for col in range(COL_SIZE):
        row = get_open_row(game_board, col)
        if row is not None:
            new_game_board = np.copy(game_board)
            new_game_board[row][col] = piece
            new_states.append(new_game_board)
    return new_states
