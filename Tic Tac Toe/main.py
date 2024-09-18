# Tic Tac Toe game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a win condition
def check_win(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([s == player for s in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full (i.e., a tie)
def check_tie(board):
    return all([s != " " for row in board for s in row])

# Function to handle player input
def get_move(player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column 1-3): ").split())
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter values between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter row and column as numbers.")

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
