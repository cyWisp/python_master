#!/usr/bin/env python 
from subprocess import Popen, PIPE

STOP = ['stop', 'soft']
LIST = ['vmrun', 'list']

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

def query_vms(list_command):
    output, error = execute(list_command)
    vms_running = int(list(output.split("\n"))[0].split(" ")[-1])
    if vms_running == 0: 
        print("[!] No virtual machines currently running...")
        exit()
    else:
        return [x for x in list(output.split("\n"))[1:] if x != ""]

if __name__ == '__main__':
    vm_list = query_vms(LIST)
    power(vm_list, STOP)
