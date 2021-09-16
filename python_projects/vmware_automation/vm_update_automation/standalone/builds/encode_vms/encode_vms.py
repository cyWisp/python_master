#!/usr/bin/env python
from sys import argv, exit
import json

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

def modify_file_name(file_name):
    if argv[1]:
        file_extension = argv[1].split(".")[-1]
        return argv[1].replace(file_extension, "json")

def read_file(file_name):
    try:
        with open(file_name, "r+") as vms:
            vm_list = [vm.strip("\n") for vm in vms.readlines()]
    except Exception as e:
        print(f"[x] Error reading vm list: {e}")
        exit()
    else: return vm_list
    finally: vms.close()

def dump_file(output_file_name, data):
    try:
        with open(f"./{output_file_name}", "w+") as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()
    else: print(f"[+] {output_file_name} written!")
    finally: json_file.close()

if __name__ == '__main__':
    validate()
    data = read_file(argv[1])
    new_file_name = modify_file_name(argv[1])
    dump_file(new_file_name, data)
