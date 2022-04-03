#!/usr/bin/env python
from subprocess import Popen, PIPE
from os import environ
import json

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def read_file(file_name):
    try:
        with open(file_name, "r+") as vms:
            vm_list = [vm.strip("\n") for vm in vms.readlines()]
    except Exception as e:
        print(f"[x] Error reading vm list: {e}")
        exit()
    else: return vm_list
    finally: vms.close()

def get_creds():
    return environ['VM_USER'], environ['VM_PASS']

def get_vms(vm_list):                                                                       
    try:                                                                                        
        with open(vm_list, 'r') as read_file:                                                   
            data = json.load(read_file)                                                         
    except Exception as e:                                                                      
        print(f"[x] Error: {e}")                                                                
        exit()                                                                                  
    else: return data                                                                           
    finally: read_file.close()