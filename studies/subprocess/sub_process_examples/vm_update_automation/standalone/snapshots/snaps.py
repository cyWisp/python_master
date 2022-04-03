#!/usr/bin/env python
import os
from subprocess import Popen, PIPE
from time import sleep
from sys import argv, exit

VM_PATH = "/home/wisp/Lab/virtual/virtual_machines"

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

def list_snapshots(vm):
    get_snapshots = ['vmrun', "listSnapshots", vm]
    output, error = execute(get_snapshots)
        
    if error: print(f"[x] Error | {name} snapshots unavailable...")
    else: return list(output.split("\n"))

def create_snapshot(vm, snap_name):
	create = ['vmrun', 'snapshot', vm, snap_name]
	output, error = execute(create)

	if error: print(f"[x] Error: {error}")
	else: print(f"[+] Snapshot {snap_name} created for {vm} successfully!")

def delete_snapshot(vm, snap_name):
	delete = ['vmrun', "deleteSnapshot", vm, snap_name]
	output, error = execute(delete)

	if error: print(f"[x] Error: {error}")
	else: print(f"[+] Snapshot {snap_name} has been deleted for {vm}...")


def usage():
	usage_string = f"""[!] Usage: {argv[0]} [-lv] <virtual machine> [operation]
Description: 

Snaps is a command line utility for managing VMware vitual machine snapshots
using the vmrun binary.

Usage Examples:

1. {argv[0]} -lv:
	List available virtual machines.
2. {argv[0]} <virtual machine name> list:
	List all snapshots for given virtual machine.
3. {argv[0]} <virtual machine name> create <snapshot name>:
	Create a new snapshot for given virtual machine with specified name.
4. {argv[0]} <virtual machine name> delete <snapshot name>:
	Delete specified snapshot for given virtual machine.
	"""
	print(usage_string)
	exit()

# argv[0] = script name
# argv[1] = vm
# argv[2] = action
# argv[3] = snapshot name (create/delete)
def validate(vm_list):
	op = list()

	# check length of arg list
	if len(argv) < 2 or len(argv) > 4:
		usage()
	else:
		# if len is 2, validate "-lv (list vms) switch was used"
		if len(argv) == 2:
			if argv[1] != "-lv":
				usage()
			else:
				op.append(argv[1])
				return op
		# length is 3, make sure argv[1] is in vm list
		elif len(argv) == 3:
			if argv[1] not in vm_list.keys() or argv[2] != "list":
				usage()
			else:
				op.append(argv[1])
				op.append(argv[2])
				return op
			# if it is in vm list, make sure argv[2] is "list", "create" or "delete"
		elif len(argv) == 4:
				if argv[2] != "create" and argv[2] != "delete":
					usage()
				else:
					op.append(argv[1])
					op.append(argv[2])
					op.append(argv[3])
					return op

def ops(vms, op):
	if op[0] == "-lv":
		print("Available Virtual Machines: ")
		for index, vm in enumerate(vms.keys()):
			print(f"{index + 1}. {vm}")
	else:
		if op[0] in vms.keys():
			if op[1] == "list":
				snaps = list_snapshots(vms[op[0]])
				sorted_snaps = [x for x in snaps if x != "" and "Total" not in x]
				
				print(f"[+] Snapshots for {op[0]}\n")
				for index, snap in enumerate(sorted_snaps):
					print(f"{index + 1}. {snap}")
			
			elif op[1] == "create":
				print("[+] Creating...")
				create_snapshot(vms[op[0]], op[2])
			elif op[1] == "delete":
				snaps = list_snapshots(vms[op[0]])
				sorted_snaps = [x for x in snaps if x != "" and "Total" not in x]

				if op[2] not in sorted_snaps:
					print("[x] Snapshot not found...")
					exit()
				else:
					print("[+] Deleting...")
					delete_snapshot(vms[op[0]], op[2])

if __name__ == '__main__':
	vms = get_vmx_files(VM_PATH)
	op = validate(vms)
	ops(vms, op)