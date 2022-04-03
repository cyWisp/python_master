#!/usr/bin/env python
import time

if __name__ == '__main__':

    start_time = time.time()
    print('start time: {:.2f}'.format(start_time))

    time.sleep(5)

    end_time = time.time()
    print('end time: {:.2f}'.format(end_time))

    total_duration = end_time - start_time
    print('Total runtime: {:.2f}s'.format(total_duration))
