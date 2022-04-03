#!/usr/bin/env python
import asyncio

async def hi_and_bye():
    print('hi there')
    await asyncio.sleep(1)
    print('okay, bye..')

async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')

async def main():
    await asyncio.gather(count(), hi_and_bye())

if __name__ == '__main__':
    asyncio.run(main())