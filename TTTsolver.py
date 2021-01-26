# Tic-Tac-Toe AI - Base Code
# By Daniel Perks

# This code is the base code, with no actual implementation
# into a game or demo. Basic commenting to explain some
# of my choices has been added too.


# Used for random move generation
import random
# Used for board index conversion
import math
# Needed to make test copy of 2D array
from copy import deepcopy


def cwRow(board):
    #
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return True
    return False


def cwCol(board):
    # Swap the axis of the 2D array
    newb = [[i[x] for i in board] for x in range(len(board))]
    # Use logic from cwRow
    for col in newb:
        if len(set(col)) == 1 and col[0] != " ":
            return True
    return False


def cwDia(board):
    ldiag = []
    rdiag = []

    # Get the diagonals and add to list
    for x in range(len(board)):
        ldiag.append(board[x][x])
        rdiag.append(board[x][(len(board) - 1) - x])

    # If either list has only one unique item, and that item is not a " ", a diag win is found
    if len(set(ldiag)) == 1 and ldiag[0] != " " or len(set(rdiag)) == 1 and rdiag[0] != " ":
        return True
    return False


def checkWin(board):
    # Runs each check win function and checks if any are True
    out = [cwRow(board), cwCol(board), cwDia(board)]
    return any(out)


def bruteWin(board, symbol, iscomp):
    # Brute forces all possible moves
    for pot in range(9):
        testboard = deepcopy(board)
        # If the space is empty
        if testboard[math.floor(pot / len(testboard))][(pot % len(testboard))] == " ":
            # ^ The math.floor code converts a square number (1-9) to an x,y coord style index
            # Take the square
            testboard[math.floor(pot / len(testboard))][(pot %
                                                         len(testboard))] = symbol
            # If the move makes a win
            if checkWin(testboard):
                # Check if this is a test for the player, not the AI
                if not iscomp:
                    # If so, invert the symbol
                    if symbol == "x":
                        new = "o"
                    else:
                        new = "x"
                    # Overwrite with AI symbol to block player
                    testboard[math.floor(pot / len(testboard))
                              ][(pot % len(testboard))] = new
                return testboard
    else:
        # If no win imminent win conditions, return None
        return None


def randomMove(board, symbol):
    freespaces = [[True if x == " " else False for x in row] for row in board]
    flatfreespaces = freespaces[0] + freespaces[1] + freespaces[2]
    choicespaces = [i for i, x in enumerate(flatfreespaces) if x]
    if len(choicespaces) > 0:
        choice = (random.choice(choicespaces))
        board[math.floor(choice / len(board))][(choice % len(board))] = symbol
        return board
    else:
        return None


def aiMove(board, symbol):
    # board should be 2D array
    # symbol = "x" | "o"

    # Finds other players symbol
    if symbol == "x":
        symbolalt = "o"
    else:
        symbolalt = "x"

    if checkWin(board):
        # game finished
        return True, board

    compwin = bruteWin(board, symbol, True)
    plyrwin = bruteWin(board, symbolalt, False)

    if compwin:
        # Taking possible win
        return True, compwin
    if plyrwin:
        # Blocking player from winning
        return False, plyrwin
    else:
        newboard = randomMove(board, symbol)
        if newboard is None:
            # Stalemate or win already occured
            return True, board
        # AI takes Random Move

        return False, newboard
