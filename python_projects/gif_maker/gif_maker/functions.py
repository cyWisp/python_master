#!/usr/bin/env python
from os import system
from time import sleep

def title_banner():
    banner = """  ________.__  _____  _____         __                 
 /  _____/|__|/ ____\/     \ ____  |  | __ ___________ 
/   \  ___|  |\  __\/  \ /  \\_   \ |  |/ // __ \_  __\\
\    \_\  \  ||  | /    Y   \/ __ \|    < \  __/|  |\/
 \______  /__||__| \____|__  (___  /__|_ \\ \\__  >__|   
        \/                 \/    \/     \/    \/       
    """
    print(f"{banner}\n\tWritten by: Wi5p\tVer. 0.1")
    print("\t--------------------------------\n")

def intro():
    system('cls')
    sleep(1)
    title_banner()

def action_messages():
    messages = {
        "check_arg_no": "[!] Checking arguments list...",
        "check_file_name": "[!] Checking for existence of requested file name...",
        "check_target_directory": "[!] Checking target directory for image files...",
        "everything_ok": "[*] OK...",
        "reading_files": "[!] Reading files...",
        "creating_gif": "[!] Creating GIF image...",
        "success": "[*] Process successful!\n",
    }

    return messages





    