#!/usr/bin/env python
if __name__ == '__main__':

    hat_list = [1, 2, 3, 4, 5]

    print(f"Give list: {hat_list}\nLength: {len(hat_list)}\n")
    
    while True:
        try:
            temp = int(input("Replacement: "))
        except ValueError as value_error:
            print("[!] Please enter an integer.")
        else:
            hat_list[2] = temp
            break

    print("[!] Removing last element!")
    del hat_list[-1]

    print(f"[!] Current list length: {len(hat_list)}")
    print(hat_list)
