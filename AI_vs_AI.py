# Tic-Tac-Toe AI - AI vs AI
# By Daniel Perks

# This is a demo where the AI plays itself.
#
# It does occasionally beat itself, when it
# randomly gets itself into a position where
# there are two win options in one turn, but
# not often as there is no logic built in
# to try to work towards this case.

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


def gameloop(board, turns):
    win, newboard1 = aiMove(board, "x")
    if win:
        return True, newboard1, turns
    print("\n\n  Turn " + str(turns) + ":")
    printBoard(newboard1)
    input()
    turns += 1
    win, newboard2 = aiMove(newboard1, "o")
    if win:
        return True, newboard2, turns
    print("\n\n  Turn " + str(turns) + ":")
    printBoard(newboard2)
    input()
    turns += 1
    return False, newboard2, turns


def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    clr()
    input("Hit enter to progress through the turns...")
    clr()
    win = False
    turns = 1
    while not win:
        win, board, turns = gameloop(board, turns)
    if win:
        print("\n\n\n\n\n")
        print("FINAL BOARD")
        print("-----------")
        printBoard(board)


main()
