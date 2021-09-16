#!/usr/bin/env python
from subprocess import Popen, PIPE
from sys import argv, exit
# from time import sleep

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

    #command.wait()

	return output, error

def read_vm_list(file_name):
    try:
        with open(file_name, "r+") as vms:
            vm_list = [vm.strip("\n") for vm in vms.readlines()]
    except Exception as e:
        print(f"[x] Error reading vm list: {e}")
        exit()
    else: return vm_list
    finally: vms.close()

def get_snapshots(vm_list):
    
    snapshots_by_host = dict()

    for vm in vm_list:
        vmrun_list_command = ["vmrun", "listSnapshots", vm]
        output, error = execute(vmrun_list_command)

        if error != "":
            print("[x] Error: {error}")
            continue
        else: pass

        if output:
            node_name = vm.split("/")[-1]
            snapshots = list(output.split("\n"))
            
            for index, snapshot in enumerate(snapshots):
                if "Total" in snapshot:
                    del snapshots[index]
                else: continue
            
            snapshots_by_host[node_name] = snapshots
    
    return snapshots_by_host

def print_snaps(node_snaps):
    for node_name, snapshot_list in node_snaps.items():
        print(f"{node_name}:\n")
        for snapshot in snapshot_list:
            print(snapshot)

def delete_excess(node_snaps, vm_list):
    # vmrun deleteSnapshot /home/wisp/Lab/virtual/virtual_machines/linux/kali/kali_2020/Kali-Linux-2020.1-vmware-amd64.vmx "UPDATE - 05_26_2020"

    node_map = {n: vm_list[i] for i, n in enumerate(node_snaps.keys())}

    # for k, v in node_map.items():
    #     print(f"{k}: {v}")

    # Clear empty list items
    for node_name, snapshot_list in node_snaps.items():
        for s in range(len(snapshot_list)):
            if snapshot_list[s] == "":
                del snapshot_list[s]

    # Delete excess snapshots    
    for node_name, snapshot_list in node_snaps.items():
        if len(snapshot_list) > 5:
            # print(f"{node_name}: {len(snapshot_list)}")
            for s in snapshot_list[5:]:
                snap = f"{s}"
                
                delete = [
                    "vmrun", 
                    "deleteSnapshot", 
                    node_map[node_name],
                    snap,
                ]

                print(delete)

                out, err = execute(delete)
                if out: print(out)
                if err: print(err)
                print(f"[+] Successfully deleted {s}")    


if __name__ == '__main__':

    vm_list = read_vm_list(argv[1])
    node_snaps = get_snapshots(vm_list)
    
    
    print_snaps(node_snaps)
    delete_excess(node_snaps, vm_list)
    new_snaps = get_snapshots(vm_list)
    
    print("UPDATED: \n\n")
    print_snaps(new_snaps)