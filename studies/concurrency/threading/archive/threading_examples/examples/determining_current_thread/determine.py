#!/usr/bin/env python
import threading, time

def worker(data):

    print(threading.current_thread().getName(), 'Starting...\nData: {0}'.format(data))
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting...')

def my_service(data):

    print(threading.current_thread().getName(), "Starting...\nData: {0}".format(data))
    time.sleep(1)
    print(threading.current_thread().getName(), "Exiting...")

if __name__ == '__main__':

    worker_1 = threading.Thread(name='worker_1', target=worker, args=('This',))
    worker_2 = threading.Thread(name='worker_2', target=worker, args=('is',))
    service_1 = threading.Thread(name='service_1', target=my_service, args=('fun!',))

    worker_1.start()
    worker_2.start()
    service_1.start()
