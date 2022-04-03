#!/usr/bin/env python
import json
from sys import argv, exit

def validate():
    try:
        if len(argv) < 2:
            print(f"[x] Usage: {argv[0]} <FILE>")
            exit()
        else:
            pass
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()

def get_vms(vm_list):
    try:
        with open(vm_list, 'r') as read_file:
            data = json.load(read_file)
            read_file.close()
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()
    else: return data
    finally: read_file.close()

def write_file():
    data = get_vms(argv[1])
    file_name = argv[1].split(".")[0] + ".txt"
    try:
        with open(file_name, 'w') as output_file:
            for line in data:
                output_file.write(line)
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()
    else: print(f"[+] {file_name} written successfully!")
    finally: output_file.close()

if __name__ == '__main__':
    validate()
    write_file()


    