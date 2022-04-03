#!/usr/bin/env python
from subprocess import Popen, PIPE
from sys import argv, exit
import json

# Requires 755 persmissions
VMS = "/usr/local/bin/vms.json"
STOP = ['stop', 'nogui']
LIST = ['vmrun', 'list']
RESET = ['vmrun', 'reset', 'soft']

def get_vms():
    vm_list = execute(LIST)[0].split("\n")
    strip = [x for x in vm_list if x != ""]

    running = int(strip[0].split(" ")[-1])

    if running == 0:
        print("[!] No virtual machines currently running...")
        exit()
    else: return {x.split("/")[-2]: x for x in strip if "Total" not in x}

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def stop_all(vm_dict, command):
    for vm in vm_dict.values():
        name = list(vm.split("/"))[-1]
        print(f"[+] Stopping {name}...")
       
        start_stop = ['vmrun', command[0], vm, command[1]]
        
        output, error = execute(start_stop)
        
        if error: print(f"[x] Error | {name} state unchanged...")
        else: print(f"[+] {name} state changed...")

def stop_single(vm, command):
    name = list(vm.split("/"))[-1]
    print(f"[+] Stopping {name}...")

    start_stop = ['vmrun', command[0], vm, command[1]]
        
    output, error = execute(start_stop)
        
    if error: print(f"[x] Error | {name} state unchanged...")
    else: print(f"[+] {name} state changed...")

def reset(vm, command):
    name = list(vm.split("/"))[-1]
    print(f"[+] Stopping {name}...")

    reset_vm = [command[0], command[1], vm, command[2]]
    output, error = execute(reset_vm)

    if error: print(f"[x] Error | {name} state unchanged...")
    else: print(f"[+] {name} state changed...")

def show_vms(vm_dict):
    print("[+] Running virtual machines:\n")
    for index, i in enumerate(vm_dict.keys()): print(f"{index + 1}. {i}")

def usage():
    print(f"[!] Usage: {argv[0]} < list | name | all >")

def validate(vm_dict):
    if len(argv) < 2 or len(argv) > 3:
        usage()
        exit()
    else:
        if argv[1] == "list": return "list"
        elif argv[1] == "all": return "all"
        elif argv[1] == "reset": return "reset"
        elif argv[1] in vm_dict.keys(): return argv[1]
        else:
            usage()
            exit()

def command(choice, vm_dict):
    if choice == "list": show_vms(vm_dict)
    elif choice == "all": stop_all(vm_dict, STOP)
    elif choice == "reset": reset(vm_dict, RESET)
    else: stop_single(vm_dict[choice], START)

if __name__ == '__main__':

    vm_dict = get_vms()
    choice = validate(vm_dict)
    command(choice, vm_dict)

