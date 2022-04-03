#!/usr/bin/env python
import subprocess

PS_PATH = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    
if __name__ == '__main__':

    command = subprocess.Popen(
        [
            PS_PATH, 
            "-ExecutionPolicy", 
            "Bypass", 
            "-NoLogo", 
            "-NoProfile", 
            "-File",
            "./wlp_csv_gen.ps1",
            "TEST_CI_FUNCTION",
            "ITS-CIP7-R1-EVD-AIX-FCS-08-06-2019.xlsx", 
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output = command.communicate()[0].decode("utf-8").strip("\n")

    print(output)
