#!/usr/bin/env python
import json
from sys import exit

PATH = "./vms.json"

def get_vms(vm_list=PATH):
    try:
        with open(vm_list, 'r') as read_file:
            data = json.load(read_file)
            read_file.close()
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()
    else: return data
    finally: read_file.close()

if __name__ == '__main__':


    print(get_vms())