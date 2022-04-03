#!/usr/bin/env python
if __name__ == '__main__':
    my_list = [8, 10, 6, 2, 4]  # list to sort
    swapped = True # set to True in order to enter an infinite loop
    
    while swapped:
        swapped = False # no swaps so far
        for i in range(len(my_list) - 1): # we only need 4 comparisons (the list length is 5)
            if my_list[i] > my_list[i + 1]: # compare adjacent elements
                # if the first is larger, swap the elements
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True # swap has occured (keep looping)
            else:
                pass

        print(my_list)

            
