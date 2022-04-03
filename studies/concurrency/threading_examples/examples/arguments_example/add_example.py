#!/usr/bin/env python
import threading

def add(num_1, num_2):

    print(threading.current_thread().getName() + " Calculation: {0}".format(str(num_1 + num_2)))

if __name__ == '__main__':

    threads = list()

    for i in range(5):

        new_thread = threading.Thread(target=add, args=(i, (i + 1),))
        threads.append(new_thread)
        new_thread.start()
