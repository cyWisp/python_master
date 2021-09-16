#!/usr/bin/env python

if __name__ == '__main__':

    hat_list = [1, 2, 3, 4, 5]

    middle_replace = int(input("Number: "))

    print(f"Initial Array: {hat_list}")
    
    print("\nReplacing the middle element with user input: ")
    hat_list[2] = middle_replace
    print(f"Replaced: {hat_list}")

    print("\nRemoving the last element in the array: ")
    del hat_list[-1]
    print(f"Removed: {hat_list}")

    print(f"\nThe length of the array is {len(hat_list)}")
