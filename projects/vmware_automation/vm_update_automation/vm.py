from utilities import (
    read_file, 
    execute,
)
from sys import exit

# ============== POWER ==============
def start(vms, start_command):
    vm_list = read_file(vms)
    power(vm_list, start_command)

def stop(vms, stop_command):
    vm_list = query_vms(vms)
    power(vm_list, stop_command)

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


# ============== INFO ==============
def get_ip_addresses(vm_list):
    vms = read_file(vm_list)
    ips = list()
    
    for vm in vms:
        get_vm_ip = ['vmrun', 'getGuestIPAddress', vm]
        output, error = execute(get_vm_ip)
        if output: ips.append(output.strip("\n"))
        if error:
            print(f"[x] Error: {error}")
            exit()
    return ips

def query_vms(list_command):
    output, error = execute(list_command)
    vms_running = int(list(output.split("\n"))[0].split(" ")[-1])
    if vms_running == 0: 
        print("[!] No virtual machines currently running...")
        exit()
    else:
        return [x for x in list(output.split("\n"))[1:] if x != ""]

