#!/usr/bin/env python
from utilities import get_creds, read_file
from paramiko import SSHClient
from os import environ

HOSTS = "/home/wisp/.ssh/known_hosts"
COMMANDS = {
    "host_name": "hostname",
    "who_am_i": "whoami",
    "update": f"echo {environ['VM_PASS']} | sudo -S apt update",
    "list_upgradable": "apt list --upgradable -a",
}

def connect(user, pw, node):
    client = SSHClient()
    client.load_host_keys(HOSTS)
    client.connect(node, username=user, password=pw)

    return client, node

def run_command(client, node, command):
    stdin, stdout, stderr = client.exec_command(command)
    return_code = stdout.channel.recv_exit_status()
    output, error = stdout.read().decode("utf-8").rstrip("\n"), stderr.read().decode("utf-8")
    
    node_log = f"{node} | {command}"
    OUTPUT[node_log] = [output, error, return_code]

    stdin.close()
    stdout.close()
    stderr.close()

    client.close()

if __name__ == '__main__':
    user, password = get_creds()
    nodes = read_file(NODES)

    client, node = connect(user, password, nodes[0])
    run_command(client, node, COMMANDS["ip_address"])
    
    for k, v in OUTPUT.items():
        print(f"{k}\n")
        print(f"output: {v[0]}\nerror:{v[1]}\nexit_status:{v[2]}")    
