# Tic-Tac-Toe AI - Player vs AI
# By Daniel Perks

# This is an actual playable game against the AI
# It's built to choice random moves unless either player has
# an immediate win on the next turn, where it will instead
# either block the player from winning, or take its own
# win opportunity.

import time
import math

from TTTsolver import aiMove, checkWin


def clr():
    print("\n"*60)


def printBoard(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")


def playerMove(board, symbol):
    count = 0
    while count < 6:
        count += 1
        clr()
        print("Current board:")
        printBoard(board)
        print("Player: " + symbol)
        if symbol == "x":
            print("Computer: o")
        else:
            print("Computer: x")
        print("\n")
        print("Choose your next position...")
        print("")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("")
        choice = input("CHOICE: ")
        if choice.isnumeric():
            choice = int(choice)
            if choice < 10 and choice > 0:
                choice -= 1
                if board[math.floor(choice / len(board))][(choice % len(board))] != " ":
                    clr()
                    print("This square is already taken - pick another...")
                    time.sleep(3)
                else:
                    board[math.floor(choice / len(board))
                          ][(choice % len(board))] = symbol
                    return board
            else:
                clr()
                print("Please pick a valid option...")
                time.sleep(3)
        else:
            print("Please pick a valid option...")
            time.sleep(3)
    clr()
    print("You did not pick a valid option")
    input("The program will now close...")


def gameloop(board, player):
    if player == "x":
        newboard1 = playerMove(board, "x")
        win, newboard2 = aiMove(newboard1, "o")
        if win:
            return True, newboard2
    else:
        win, newboard1 = aiMove(board, "x")
        if win:
            return True, newboard1
        newboard2 = playerMove(newboard1, "o")

    if checkWin(newboard2):
        return True, newboard2
    else:
        return False, newboard2


def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    clr()
    start = input("Do you want to start first (y/n): ")
    if start.lower() == "y" or start.lower() == "yes":
        player = "x"
    else:
        player = "o"
    win = False
    while not win:
        win, board = gameloop(board, player)
    if win:
        clr()
        print(" GAME OVER ")
        print("-----------")
        printBoard(board)


main()
