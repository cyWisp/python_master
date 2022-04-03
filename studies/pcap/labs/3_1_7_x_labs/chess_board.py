#!/usr/bin/env python
if __name__ == '__main__':


    # Using standard for with list comprehension
    board = []
    for i in range(8):
        row = [x for x in range(8)]
        board.append(row)

    for row in board:
        print(row)

    print("\n\n")

    # Using nested list comprehensions
    board_2 = [[x for x in range(8)] for j in range(8)]

    for row in board_2:
        print(row)
