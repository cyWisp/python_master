#!/usr/bin/env python
import threading

def worker():

    #thread worker function
    print('Worker')
    return

if __name__ == '__main__':

    threads = []
    for t in range(5):
        new_thread = threading.Thread(target=worker)
        threads.append(new_thread)
        new_thread.start()