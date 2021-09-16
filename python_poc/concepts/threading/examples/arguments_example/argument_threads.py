#!/usr/bin/env python
import threading

def worker(num):
    # thread worker function_1
    print("Worker {0}".format(num))

if __name__ == '__main__':

    threads = []

    for i in range(3):
        new_thread = threading.Thread(target=worker, args=(i,))
        threads.append(new_thread)
        new_thread.start()
