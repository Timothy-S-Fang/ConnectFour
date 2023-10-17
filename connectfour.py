import numpy as np
from minimax import minimax
import unittest


ROW_SIZE = 6
COL_SIZE = 7
board_size = (ROW_SIZE, COL_SIZE) #size of the columns, rows
cell_empty = 0 #empty cell on board
player_x = 1 #player x piece on board
player_y = 2 #player y piece on board
game_over = False
turn = 0

game_board = np.zeros(board_size, dtype=int)

def create_board():
    """A function to initalize the board."""
    global game_board
    game_board = np.zeros(board_size, dtype=int)

def player_turn(board, row, col, piece):
    """A function allowing the player to make a move."""
    board[row][col] = piece

def valid_move(board, col):
    """A function to check whether a move is valid/legal.
    Returns True if the move is within the grid and is not
    already filled."""
    if 0 <= col < COL_SIZE:
        return board[-1][col] == 0
    return False

def print_board():
    """Prints the game-board."""
    print(np.flipud(game_board))

    return

def game_progress():
    """A function thath checks if the game has been won by a certain player
    and is run every time move is made (see main).
    Returns True or False to adjust game_over."""
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                game_board[row][col + 1] == player
                and game_board[row][col + 2] == player
                and game_board[row][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a horizontal connection!")
                print_board()
                return True

    # Vertical win
    for col in range(COL_SIZE):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                game_board[row + 1][col] == player
                and game_board[row + 2][col] == player
                and game_board[row + 3][col] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a vertical connection!")
                print_board()
                return True

    # Positively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(ROW_SIZE - 3):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                col + 3 < COL_SIZE
                and game_board[row + 1][col + 1] == player
                and game_board[row + 2][col + 2] == player
                and game_board[row + 3][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                print_board()
                return True

    # Negatively sloped angles
    for col in range(COL_SIZE - 3):
        for row in range(3, ROW_SIZE):
            if game_board[row][col] == cell_empty:
                break
            player = game_board[row][col]
            if (
                game_board[row - 1][col + 1] == player
                and game_board[row - 2][col + 2] == player
                and game_board[row - 3][col + 3] == player
            ):
                print("Congratulations! Player " + str(player) + " has won the game on a diagonal connection!")
                print_board()
                return True

    return False

def get_open_row(col):
    """Returns the next open row given a column from top down."""
    for row in range(ROW_SIZE):
        if game_board[row][col] == cell_empty:
            return row
    return

if __name__ == '__main__':
    while not game_over:

        print_board()

        # Player one turn
        if turn == 0:
            while True:
                try:
                    col = int(input("Player 1, choose your move from (0-6): "))
                    if 0 <= col <= 6 and valid_move(game_board, col):
                        break  # Valid input, exit the loop
                    else:
                        print("Invalid input. Choose your move from (0-6): ")
                except ValueError:
                    print("Invalid input. Choose your move from (0-6): ")
            row = get_open_row(col)
            player_turn(game_board, row, col, player_x)

        # Player two turn
        else:
            col = minimax(game_board, depth = 5, alpha=float('-inf'), beta=float('inf'),  Maximizing=True)[1]
            row = get_open_row(col)
            player_turn(game_board, row, col, player_y)
            print("AI choose to play " + str(col))
            
        game_over = game_progress()
        turn += 1
        turn = turn % 2
        
        # Check for a draw condition (board full)
        if np.all(game_board != cell_empty):
            print("The game is a draw!")
            break

class TestConnectFour(unittest.TestCase):
    def test_create_board(self):
        # Test if the create_board function initializes the game board properly
        create_board()
        self.assertTrue(np.array_equal(game_board, np.zeros((6, 7), dtype=int)))

    def test_player_turn(self):
        # Test if the player_turn function correctly updates the game board
        create_board()
        player_turn(game_board, 5, 3, 1)
        self.assertEqual(game_board[5][3], 1)  # Ensure the specified position is updated

    def test_valid_move(self):
        # Test if the valid_move function correctly checks if a move is valid
        create_board()
        self.assertTrue(valid_move(game_board, 3))  # Column 3 should be valid
        player_turn(game_board, 5, 3, 1)  # Fill a slot in column 3
        self.assertFalse(valid_move(game_board, 3))  # Column 3 should be invalid after the move
        
if __name__ == '__main__':
    unittest.main()

