#!/usr/bin/env python
import threading, time

def worker():

    print(threading.currentThread().getName(), 'Starting...')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting...')

def service():

    print(threading.currentThread().getName(), 'Starting...')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting...')

if __name__ == '__main__':

    worker_1 = threading.Thread(name='worker_1', target=worker)
    worker_2 = threading.Thread(name='worker_2', target=worker)
    service_1 = threading.Thread(name='service_1', target=service)
    nameless = threading.Thread(target=service) #use the default name

    worker_1.start()
    worker_2.start()
    service_1.start()
    nameless.start()