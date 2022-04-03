#!/usr/bin/env python
from subprocess import Popen, PIPE
from sys import exit
import json

# Requires 755 persmissions
VMS = "/usr/local/bin/vms.json"
START = ['start', 'nogui']

def get_vms(vm_list=VMS):
    try:
        with open(vm_list, 'r') as read_file:
            data = json.load(read_file)
    except Exception as e:
        print(f"[x] Error: {e}")
        exit()
    else: return data
    finally: read_file.close()

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def power(vm_list, command):
    results = dict()

    for vm in vm_list:
        name = list(vm.split("/"))[-1]
        if command[0] == 'start': print(f"[+] Starting {name}...")
        if command[0] == 'stop': print(f"[+] Stopping {name}...")
        
        start_stop = ['vmrun', command[0], vm, command[1]]
        
        output, error = execute(start_stop)
        
        if error: print(f"[x] Error | {name} state unchanged...")
        else: print(f"[+] {name} state changed...")

if __name__ == '__main__':
    
    vm_list = get_vms()
    power(vm_list, START)

