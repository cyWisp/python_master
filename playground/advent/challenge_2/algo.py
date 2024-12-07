
def desc_arr_test(arr):
    desc = True

    print(arr)
    for i in range(len(arr) - 1):
        try:
            print(f'Comparing {arr[i]} and {arr[i + 1]}')
            if arr[i] > arr[i + 1]:
                pass

            elif arr[i] == arr[i + 1]:
                print(f'Removing {arr[i + 1]} and rerunning function.')

                desc = False
                arr.remove(arr[i + 1])
                desc_arr_test(arr)

            else:
                desc = False

        except IndexError:
            break

    print(desc)


if __name__ == '__main__':
    arr = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    test = [10, 7, 7, 6, 4, 2, 1]

    desc_arr_test(test)