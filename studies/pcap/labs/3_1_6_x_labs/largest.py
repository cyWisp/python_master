#!/usr/bin/env python
if __name__ == '__main__':

    myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = myList[0]

    for i in range(1, len(myList)):
        if myList[i] > largest:
            largest = myList[i]

    print(largest)

    list_2 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest_2 = list_2[0]

    for i in list_2:
        if i > largest_2:
            largest_2 = i

    print(largest_2)

    # Using a slice
    
    list_3 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest_3 = list_3[0]

    for x in list_3[1:]:
        if x > largest_3:
            largest_3 = x

    print(largest_3)
