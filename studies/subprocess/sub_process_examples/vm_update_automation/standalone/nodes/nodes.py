#!/usr/bin/env python
from subprocess import Popen, PIPE

LIST = ['vmrun', 'list']

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

def get_ip_addresses(vm_dict):
    ips = dict()

    for name, file in vm_dict.items():
        get_vm_ip = ['vmrun', 'getGuestIPAddress', file]
        output, error = execute(get_vm_ip)
        if output: ips[name] = output.strip("\n")
        if error:
            print(f"[x] Error: {error}")
            exit()
    return ips

def run():
    running = get_vms()
    ips = get_ip_addresses(running)

    print("[+] Running VMs: \n")
    for k, v in ips.items(): print(f"[+] {k}: {v}")

if __name__ == '__main__':
    run()