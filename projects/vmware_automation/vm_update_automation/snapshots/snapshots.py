#!/usr/bin/env python
from vm import query_vms, list_snapshots
from utilities import get_vms
from menu import print_header
from time import sleep
from os import system
from sys import exit

VMS = "/usr/local/bin/vms.json"

def clean_snaps(snaps):
    for snap in snaps.values():
        for index, s in enumerate(snap):
            if len(s) == 0:
                del snap[index]
    return snaps
            
def print_snaps(vm_list, snaps):
    for name, snap_list in snaps.items():
        snap_count = snap_list[0].split(" ")[2]
        print(f"*** SNAPSHOTS: {name} [{snap_count}] ***")
        for index, snap in enumerate(snap_list[1:]):    
            print(f"{index + 1}. {snap}")
        print()

def get_snaps(vm_list):
    snaps = list_snapshots(vm_list)
    cleaned_snaps = clean_snaps(snaps)
    return cleaned_snaps

def validate(choice, menu_length):
    try:
        int_choice = int(choice)
    except ValueError: return False
    else: 
        if int_choice < 1 or int_choice > (menu_length + 2):
            return False
        else: return True

def main_menu(snaps):
    while True:
        system('clear')
        print_header()
        
        for index, name in enumerate(snaps.keys()):
            print(f"{index + 1}. {name}")
        print("6. Exit")
        
        choice = input("\n[+] Selection: ")
        val = validate(choice, len(snaps.keys()))
        
        if val == False:
            print("[x] Please make a valid selection...")
            sleep(2)
            continue
        
        else: 
            print(choice)
            sleep(2)


if __name__ == '__main__':

    vm_list = get_vms(VMS)
    snaps = get_snaps(vm_list)
    main_menu(snaps)