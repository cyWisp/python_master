#!/usr/bin/env python
import os
from sys import argv, exit
from subprocess import Popen, PIPE

VM_PATH = "/home/wisp/Lab/virtual/virtual_machines"

def get_creds():
    return environ['VM_USER'], environ['VM_PASS']

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def get_vmx_files(path):
	vmx_files = dict()
	for root, dirs, files in os.walk(path):
		for name in files:
			if name[-3:] == "vmx": 
				vmx_files[name[:-4]] = os.path.join(root, name)

	return vmx_files

def get_ip_addresses(vms):
    ip_map = dict()
    for name, file in vms.items():
        get_vm_ip = ['vmrun', 'getGuestIPAddress', file]
        output, error = execute(get_vm_ip)
        if "Error" not in output and not error: ip_map[name] = output.strip("\n")
        else: continue
    return ip_map

def usage():
	usage_string = f"""[!] Usage: {argv[0]} [-lv] <virtual machine> [operation]
[?] Description: 

Snaps is a command line utility for managing VMware vitual machine snapshots
using the vmrun binary.

[?] Usage Examples:

1. {argv[0]} -lv:
	List available virtual machines.
2. {argv[0]} <virtual machine name> check:
	Check if updates are available for given virtual machine.
3. {argv[0]} <virtual machine name> update:
	Update the specified virtual machine.
	"""
	print(usage_string)
	exit()

# argv[0] = script name
# argv[1] = vm | -lv (list vms)
# argv[2] = action [check | update]
def validate(vm_list):
    op = list()

    # check length of arg list
    if len(argv) < 2 or len(argv) > 3:
        usage()
    else:
        # if len is 2, validate "-lv (list vms) switch was issued"
        if len(argv) == 2:
            if argv[1] != "-lv":
                usage()
            else:
                op.append(argv[1])
                return op
        # if length is 3, make sure argv[1] is in vm list
        elif len(argv) == 3:
            if argv[1] not in vm_list.keys():
                usage()
            if argv[2] != "check" and argv[2] != "update":
                usage()
                op.append(argv[1])
                op.append(argv[2])
        return op



if __name__ == '__main__':
    vms = get_vmx_files(VM_PATH)
    ips = get_ip_addresses(vms)
    
    # op = validate(vms)

    for k, v in ips.items():
        print(f"{k}: {v}")
    
    


