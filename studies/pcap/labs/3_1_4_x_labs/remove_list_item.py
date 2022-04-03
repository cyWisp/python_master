#!/usr/bin/env python

if __name__ == '__main__':

    nums = [x for x in range(1, 6)]

    print("Current list: ")
    [print(x) for x in nums]

    print("Removing the third element: ")
    del nums[2]

    print("Printing the edited list: ")
    [print(x) for x in nums]
