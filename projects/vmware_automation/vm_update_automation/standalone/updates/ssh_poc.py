#!/usr/bin/env python
from paramiko import SSHClient
from os import environ

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
    