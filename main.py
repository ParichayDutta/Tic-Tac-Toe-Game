def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return all(spot != " " for spot in board)

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Try again.")
                continue

            board[move] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")





tic_tac_toe()
