#!/usr/bin/env python3

#
# Tictacktoe_v2.py
#

from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    #Upper frame
    print("+-------+-------+-------+")

    column_counter = 1
    for row in board:
        if column_counter in [1, 4, 7]:
            # Blank row
            print("|       |       |       |")

        for column in row:
            # Generates de data row in-line
            print("|", end='')
            if column not in ['O', 'X']:
                print("   ", column_counter, sep='', end="   ")
            else:
                print("   ", column, sep='', end='   ')

            if column_counter in [3, 6, 9]:
                print("|\n", end='')

            column_counter += 1

        # Blank row
        print("|       |       |       |")
        # Lower frame
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.

    free_fields = make_list_of_free_fields(board)

    move_ok = False
    while not move_ok:
        field = int(input("Enter field number: "))
        if field not in range(1, 10):
            print("Value out of scope, please try again")
            continue

        move = rev_field_dictionary[field]

        if move in free_fields:
            board[move[0]][move[1]] = 'O'
            move_ok = True

    display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    list_of_free_fields     = []

    row_counter             = 0
    column_counter          = 0

    for row in board:
        for column in row:
            if column not in ["X", "O"]:
                list_of_free_fields.append((row_counter, column_counter))

            column_counter += 1

        row_counter     += 1
        column_counter  = 0

    return list_of_free_fields


def make_field_dictionary(board):
    dictionary = {}

    counter = 1
    for field in make_list_of_free_fields(board):
        dictionary.update({field: counter})
        counter += 1

    return dictionary


def make_rev_field_dictionary(board):
    dictionary = {}

    counter = 1
    for field in make_list_of_free_fields(board):
        dictionary.update({counter: field})
        counter += 1

    return dictionary


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    player_list_moves = []

    victory_cases_list  = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    # All the horizontals
    for row in range(3):
        for column in range(3):
            if board[row][column] == sign:
                player_list_moves.append(field_dictionary[(row, column)])

        if player_list_moves in victory_cases_list:
            if   sign == "X":
                print("Computer won")
            elif sign == "O":
                print("Human won")

            return True

        player_list_moves.clear()


    # All the verticals
    for column in range(3):
        for row in range(3):
            if board[row][column] == sign:
                player_list_moves.append(field_dictionary[(row, column)])

        if player_list_moves in victory_cases_list:
            if   sign == "X":
                print("Computer won")
            elif sign == "O":
                print("Human won")

            return True

        player_list_moves.clear()

    # Diagonal 1
    column = 0
    for row in range(3):
        if board[row][column] == sign:
            player_list_moves.append(field_dictionary[(row, column)])

        if player_list_moves in victory_cases_list:
            if   sign == "X":
                print("Computer won")
            elif sign == "O":
                print("Human won")

            return True

        column += 1

    player_list_moves.clear()

    # Diagonal 2
    column = 2
    for row in range(3):
        if board[row][column] == sign:
            player_list_moves.append(field_dictionary[(row, column)])

        if player_list_moves in victory_cases_list:
            if   sign == "X":
                print("Computer won")
            elif sign == "O":
                print("Human won")

            return True

        column -= 1

    player_list_moves.clear()

    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_fields = make_list_of_free_fields(board)

    move_ok = False
    while not move_ok:
        row = randrange(0, 3)
        column = randrange(0,3)
        coordinates = (row, column)

        if coordinates in free_fields:
            board[row][column] = 'X'
            move_ok = True

    display_board(board)

# --MAIN--
# Builds a list which represents the board with all the fields free.
board_list = [[' ' for j in range(3)] for i in range(3)]
# Create field coordenates dictionaries
field_dictionary        = make_field_dictionary(board_list)
rev_field_dictionary    = make_rev_field_dictionary(board_list)
# First move. Always computer starts at 1x1.
board_list[1][1] = "X"
# Display the board
display_board(board_list)

winner = False
while not winner:
    # User moves
    enter_move(board_list)
    winner = victory_for(board_list, "O")

    if winner:
        break

    # Machine moves
    draw_move(board_list)
    winner = victory_for(board_list, "X")

    if winner:
        break
