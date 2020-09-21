board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
gameon = True
winner = None
current = "X"
player_1=""
player_2=""
check=""
def play_game():
    name_input()
    name_check()
    display_board()
    while gameon:
        handle_turn(current)
        check_gameover()
        flip_p()
    if winner == "X" :
        print(player_1 + " won.")
    elif winner== "O":
        print(player_2 + " won.")
    elif winner == None:
        print("Tie.")
    z=input("Would like to play again ? (Y/N)")
    if z=='Y':
        play_game()
    else:
        print("Bye")
def name_input():
    global player_1
    global player_2
    player_1 = input("Enter a name for the X player:")
    player_2 = input("Enter a name for the 0 player:")
def name_check():
    global current
    check = input("Who plays first" + " " + player_1 + " or " + player_2 + "?")
    for i in range(1, 100, 1):
        print(check+","+player_1)
        if check!=player_1 and check!=player_2:
            print(check + "is not a registered player")
        else:
            break
        check = input("Who plays first " + player_1 + " or " + player_2 + "?")
    if check == player_1:
        current = "X"
    elif check == player_2:
        current = "O"
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")
def handle_turn(p):
    print(p + "'s turn.")
    pos = input("Choose a pos from 1-9: ")
    valid = False
    while not valid:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("Choose a pos from 1-9: ")
        pos = int(pos) - 1
        if board[pos] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[pos] = p
    display_board()
def check_gameover():
    check_winner()
    check_tie()
def check_winner():
    global winner
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
def check_rows():
    global gameon
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        gameon = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_columns():
    global gameon
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        gameon = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
def check_diagonals():
    global gameon
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        gameon = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None
def check_tie():

    global gameon
    if "-" not in board:
        gameon = False
        return True
    else:
        return False
def flip_p():
    global current
    if current == "X":
        current = "O"
    elif current == "O":
        current = "X"
play_game()