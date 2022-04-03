#!/usr/bin/env python
import threading

def worker(num):

    #thread worker function
    print("This is worker {0}".format(num))
    return #returns 'None'

if __name__ == '__main__':

    #args is in the form of a tuple

    threads = []
    for t in range(5):
        new_thread = threading.Thread(target=worker, args=(t,))
        threads.append(new_thread)
        new_thread.start()