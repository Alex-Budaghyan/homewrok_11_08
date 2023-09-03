def print_board(board):
    print('- - - - - - -')
    for row in range(3):
        print('| ', end='')
        for column in range(3):
            print(board[row][column], end=' | ')
        print('\n- - - - - - -')


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, choose a row (0-2): "))
            col = int(input(f"Player {current_player}, choose a column (0-2): "))
        except ValueError:
            print('The coordinates must be integers from 0 to 2. Please try again...')
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("The game is a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")


main()
