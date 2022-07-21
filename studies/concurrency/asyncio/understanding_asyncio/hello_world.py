#!/usr/bin/env python
import asyncio, time

async def print_nums():
    current_value = None

    for i in range(5):
        print(i)
        current_value = i

    return current_value

async def main():
    print(f'{time.ctime()} Hello!')
    some_var = await print_nums()
    print(f'{time.ctime()} Goodbye!')
    print(f'some var: {some_var}')

if __name__ == '__main__':
    asyncio.run(main())