#!/usr/bin/env python
from paramiko import SSHClient
from os import environ
import pysftp, json

TARGETS = "./targets.json"
USER = environ['VM_USER']
PASS = environ['VM_PASS']
HOSTS = '/home/wisp/.ssh/known_hosts'

def get_targets():
    print("[+] Reading targets.json")
    try:
        with open(TARGETS, 'r') as targets_file:
            targets = json.load(targets_file)
    except BaseException as e: print(f"[x] Error: {e}")
    else: return targets

def put_file(targets):
    print("[+] Uploading install script...")
    success_var = list()

    for target in targets:
        try:
            with pysftp.Connection(
                target,
                username=USER,
                password=PASS,
        ) as sftp:
                with sftp.cd("/home/wisp/"):
                    sftp.put("./install_vmtools.sh")
        except Execption as e:
            print(f"[x] Error: {e}")
            success_var.append(False)
        else:
            print("[+] File transfer successful!")
            success_var.append(True)
    if success_var[0] and success_var[1]: return True
    else: return False

def run_script(targets):
    print("[+] Running install script...")
    for target in targets:
        client = SSHClient()
        client.load_host_keys(HOSTS)
        client.connect(
            target,
            username=USER,
            password=PASS,
        )
        
        run_script = "bash /home/wisp/install_vmtools.sh"
        stdin, stdout, stderr = client.exec_command(run_script)

        # Print any output or errors as they arise
        if stdout: print(stdout.read().decode("utf-8"))
        if stderr: print(stderr.read().decode("utf-8"))

        # Get recturn code
        print(f"\nReturn Code: {stdout.channel.recv_exit_status()}")

        # Close all file objects
        stdin.close()
        stdout.close()
        stderr.close()

        client.close()

        print(f"[+] Process for host {target} completed!")

if __name__ == '__main__':
    targets = get_targets()
    file_transfer = put_file(targets)
    if file_transfer:
        run_script(targets)
