#!/usr/bin/env python
import socket

def main():

	#create an INET, STREAMing socket
	thisSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#now connect to a web server on port 80
	#typical http port
	thisSocket.connect(("www.google.com", 80))

	

if __name__=='__main__':
	main()
