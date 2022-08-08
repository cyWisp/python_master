#!/usr/bin/env python
from concurrent.futures import ThreadPoolExecutor

def worker(data, name):
    for x in range(20):
        print(f'{data} {name}: {x}', end='')



if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as x:
        for _ in range(10):
            future = x.submit(worker, 'Worker', _)
