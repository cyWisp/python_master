#!/usr/bin/env python
import socket

def main():

	#create the AD_INET streaming socket
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#bind the socket to a public host,
	#and a well-known port
	serverSocket.bind((socket.gethostname(), 80))

	#become a server socket
	serversocket.listen(5)

	while True:

		#accept connections from outside
		(clientsocket, address) = serverSocket.accept()

		#now do something with the clientsocket
		#in this case, we'll pretend this a threaded server
		ct = client_thread(clientsocket)
		ct.run()
	
	

if __name__=='__main__':
	main()
