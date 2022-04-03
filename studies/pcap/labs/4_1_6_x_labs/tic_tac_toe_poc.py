#!/usr/bin/env python
from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


if __name__ == '__main__':

    board = [[3 * j + i + 1 for i in range(3)] for j in range(3) ]
    board[1][1] = 'X'

    display_board(board)