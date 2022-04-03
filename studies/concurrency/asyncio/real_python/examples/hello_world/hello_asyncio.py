#!/usr/bin/env python

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    import time
    start = time.perf_counter()

    asyncio.run(main())

    end = time.perf_counter()

    print(f'{__file__} executed in {end:0.2f} seconds...')