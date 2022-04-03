#!/usr/bin/env python
if __name__ == '__main__':

    my_list = [8, 10, 6, 2, 4]
    swapped = True
    iteration_count = 0

    print(f"Sorting: {my_list}\n")

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                print(f"Swapping {my_list[i]} | {my_list[i+1]}")
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
            else:
                pass
        iteration_count += 1
        print(f"iteration: {iteration_count}: {my_list}")
