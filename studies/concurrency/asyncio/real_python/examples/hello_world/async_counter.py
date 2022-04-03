#!/usr/bin/env python
import asyncio
import os

async def count_to_a_million():
    for i in range(0, 99):
        print(i)


async def wait_for_count():
    print('starting count')
    await asyncio.sleep(1)
    print('done')

async def main():
    await asyncio.gather(wait_for_count(), count_to_a_million())

if __name__ == '__main__':
    asyncio.run(main())