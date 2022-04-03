#!/usr/bin/env python

if __name__ == '__main__':

    # Copying the whole list, using a slice
    list_1 = [1]
    list_2 = list_1[:]

    # Changing the first element of list 1
    list_1[0] = 2

    # Proves that list_2 remains unchanged
    # And that it is its own entity
    print(list_2)




    


