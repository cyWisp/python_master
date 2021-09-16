#!/usr/bin/env python
from tcp import Client

if __name__ == '__main__':

    new_tcp = Client('www.cybersherpa.net', 80)
    new_tcp.s_create()
    new_tcp.s_connect()
    new_tcp.s_send()
    new_tcp.s_receive()

    print(new_tcp.response)