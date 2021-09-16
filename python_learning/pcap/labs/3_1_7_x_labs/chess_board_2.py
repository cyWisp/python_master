#!/usr/bin/env python

if __name__ == '__main__':

    board = [['ROOK' if r == 0 or r ==7 else "EMPTY" for r in range(8)] for c in range(8)]

#    board[0][0], board[0][7] = "ROOK", "ROOK"
#    board[7][0], board[7][7] = "ROOK", "ROOK"

    for row in board:
        print(row)

    

