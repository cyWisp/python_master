#!/usr/bin/env python
import concurrent.futures

def some_func(name):
    greeting = f"hello {name}"
    return greeting

if __name__ == '__main__':

    names = ['rob', 'justin', 'bill', 'sam']
    greetings = list()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for name in names:
            future = executor.submit(some_func, name)
            return_value = future.result()
            greetings.append(return_value)

    for g in greetings: print(g)

