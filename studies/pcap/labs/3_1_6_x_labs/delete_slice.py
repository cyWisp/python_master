#!/usr/bin/env python

if __name__ == '__main__':

    # Deleting the whole list via slice will delete the list's contents
    # Whereas deleting the list itself will delete the list object from
    # memory completely

    this_list = [2, 3, 4, 5, 6, 7, 8]

    print(f"this list: {this_list}")

    # delete the list contents
    del this_list[:]

    print(f"this list: {this_list}")

    # delete the list from memory
    del this_list

    try:
        print(f"this list: {this_list}")
    except NameError as err:
        print("The list does not exist\nError: {0}".format(err))
    
