'''
Write a python function that will produce numbers in the following sequence, given an input variable i:

input: 0 output: 7
input: 1 output: 11 -> + 10
input: 2 output: 12 -> + 10
input: 3 output: 11 -> + 8
input: 4 output: 15 -> + 11
input: 5 output: 16 -> + 11
input: 6 output: 15 -> + 9
input: 7 output: 19 -> + 12
input: 8 output: 20 -> + 12
input: 9 output: 19 -> + 10
input: 10 output: 23 -> + 13
input: 11 output: 24 -> + 13
The function should continue the sequence and be callable with any value under 1000.
'''

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()

def log_number(i: int) -> None:
    print(i)


if __name__ == '__main__':
    num = None

    while True:
        try:
            num = int(input('Limit: '))

            if num > 1000 or num < 1:
                raise ValueError
            break
        except ValueError:
            log.error('Please enter a value between 1 and 1000')
            continue

    interval_1, interval_2, interval_count = 7, 10, 0

    for i in range(num):
        if i % 3 == 0:
            log.info(f'{i} (+{interval_1}): {i + interval_1}')
            interval_1 += 1

        else:
            log.info(f'{i} (+{interval_2}): {i + interval_2}')
            interval_count += 1

            if interval_count == 2:
                interval_count = 0
                interval_2 += 1





