# Tic-Tac-Toe AI using Minimax
# Final polished version

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def show_positions():
    print("Board Positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9\n")


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, False)
                    board[r][c] = " "
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = 1000
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, True)
                    board[r][c] = " "
                    if score < best_score:
                        best_score = score
        return best_score


def find_best_move(board):
    best_score = -1000
    best_move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "X"
                score = minimax(board, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move


def play_game():
    board = [[" "]*3 for _ in range(3)]

    show_positions()

    while True:
        print_board(board)

        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                row = (move - 1) // 3
                col = (move - 1) % 3

                if board[row][col] != " ":
                    print("That position is already occupied.")
                    continue

                board[row][col] = "O"
                break
            except ValueError:
                print("Please enter a valid number.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print("AI played.\n")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
