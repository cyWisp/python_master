#!/usr/bin/env python
from vm import (
    start,
    get_ip_addresses
)
from time import sleep

VM_FILES = {
    "vm_list": "./virtual_machines.txt",
}
VM_COMMANDS = {
    "start" : ['start', 'nogui'],
    "stop" : ['stop', 'soft'],
    "list" : ['vmrun', 'list'],
}

def startup():
    # Starts all VMs in vm_list ('virtual_machines.txt')
    # and gathers their IP addresses
    start(VM_FILES['vm_list'], VM_COMMANDS['start'])
    sleep(30)
    ips = get_ip_addresses(VM_FILES['vm_list'])

    return ips

if __name__ == '__main__':
    ips = startup()
