#!/usr/bin/env python
if __name__ == '__main__':

    chess_board = [['EMPTY' for x in range(8)] for j in range(8)]

    # Add rooks
    chess_board[0][0] = "ROOK"
    chess_board[0][7] = "ROOK"
    chess_board[7][0] = "ROOK"
    chess_board[7][7] = "ROOK"

    # Add knights
    chess_board[0][1] = "KNIGHT"
    chess_board[0][6] = "KNIGHT"
    chess_board[7][1] = "KNIGHT"
    chess_board[7][6] = "KNIGHT"

    # Add bishops
    chess_board[0][2] = "BISHOP"
    chess_board[0][5] = "BISHOP"
    chess_board[7][2] = "BISHOP"
    chess_board[7][5] = "BISHOP"

    # Add kingd and queens
    chess_board[0][3] = "BQUEEN"
    chess_board[0][4] = "BKING"
    chess_board[7][3] = "WQUEEN"
    chess_board[7][4] = "WKING"


    for row in chess_board:
        print(row)


