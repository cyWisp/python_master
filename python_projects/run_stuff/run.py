#!/usr/bin/env python
import subprocess

class Run():

    def __init__(self):

        self.powershell_path = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
        self.command_line_path = "C:\\WINDOWS\\system32\\cmd.exe"
        self.output = ""

    def pShell(self, script):

        command = subprocess.Popen([self.powershell_path, "-ExecutionPolicy", "Unrestricted", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.output = command.communicate()[0]
        self.output = self.output.decode("utf-8").strip("\n")
        
    def cmdShell(self, script):

        command = subprocess.Popen([self.command_line_path, script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.output = command.communicate()[0]
        self.output = self.output.decode("utf-8").strip("\n")
        
