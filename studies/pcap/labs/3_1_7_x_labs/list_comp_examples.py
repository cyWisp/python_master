#!/usr/bin/env python
if __name__ == '__main__':

    # Example 1 - A simple range
    row = [i for i in range(8)]
    print(row)

    # Example 2 - squares
    squares = [i ** 2 for i in range(10)]
    print(squares)

    # Example 3 - powers of 2
    twos = [2 ** i for i in range(8)]
    print(twos)

    # Example 4 - odds
    odds = [x for x in range(10) if x % 2 != 0]
    print(odds)

