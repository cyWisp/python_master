#!/usr/bin/env python
import threading, time

def worker_1():

    print(threading.current_thread().getName(), "Starting...")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting...")

def worker_2():

    print(threading.current_thread().getName(), "Starting...")
    time.sleep(0.3)
    print(threading.current_thread().getName(), "Exiting...")

if __name__ == '__main__':

    services = list()

    named_worker_1 = threading.Thread(name='service_1', target=worker_1)
    services.append(named_worker_1)
    named_worker_2 = threading.Thread(name='service_2', target=worker_2)
    services.append(named_worker_2)
    default_named_worker = threading.Thread(target=worker_1)
    services.append(default_named_worker)

    for service in services:
        service.start()
