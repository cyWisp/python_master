#!/usr/bin/env python

if __name__ == '__main__':

    my_list = [8, 10, 6, 2, 4]  # List to sort
    swapped = True  # Set to True to allow the while loop to run

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1): # we need (5 - 1) comparisons
            if my_list[i] > my_list[i + 1]:
                swapped = True  # swap occured!

                # perform the swap
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print(my_list)
        

