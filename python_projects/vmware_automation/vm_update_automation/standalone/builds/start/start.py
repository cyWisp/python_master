#!/usr/bin/env python
from subprocess import Popen, PIPE
from sys import argv, exit
import os

START = ['start', 'nogui']
VMX_FILES = "/home/wisp/Lab/virtual/virtual_machines"

def get_vmx_files(path=VMX_FILES):
    vmx_files = dict()
    
    for root, dirs, files in os.walk(path):
        for name in files:
            if name[-3:] == "vmx":
                vmx_files[name[:-4]] = os.path.join(root, name)
    
    return vmx_files

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def start_all(vm_dict, command):
    for vm in vm_dict.values():
        name = list(vm.split("/"))[-1]
        print(f"[+] Starting {name}...")
       
        start_stop = ['vmrun', command[0], vm, command[1]]
        
        output, error = execute(start_stop)
        
        if error: print(f"[x] Error | {name} state unchanged...")
        else: print(f"[+] {name} state changed...")

def start_single(vm, command):
    name = list(vm.split("/"))[-1]
    print(f"[+] Starting {name}...")

    start_stop = ['vmrun', command[0], vm, command[1]]
        
    output, error = execute(start_stop)
        
    if error: print(f"[x] Error | {name} state unchanged...")
    else: print(f"[+] {name} state changed...")

def show_vms(vm_dict):
    print("[+] Available virtual machines:\n")
    for index, i in enumerate(vm_dict.keys()): print(f"{index + 1}. {i}")

def usage():
    print(f"[!] Usage: {argv[0]} < list | name | all >")

def validate(vm_dict):
    if len(argv) != 2:
        usage()
        exit()
    else:
        if argv[1] == "list": return "list"
        elif argv[1] == "all": return "all"
        elif argv[1] in vm_dict.keys(): return argv[1]
        else:
            usage()
            exit()

def command(choice, vm_dict):
    if choice == "list": show_vms(vm_dict)
    elif choice == "all": start_all(vm_dict, START)
    else: start_single(vm_dict[choice], START)

if __name__ == '__main__':
    
    vms = get_vmx_files()
    choice = validate(vms)
    command(choice, vms)

