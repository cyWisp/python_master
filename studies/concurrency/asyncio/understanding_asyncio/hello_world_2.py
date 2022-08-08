#!/usr/bin/env python

import asyncio, time

async def loop_nums():
    for i in range(3):
        print(f'Num: {i}')


async def main():
    print(f'{time.ctime()} Hello!')
    await loop_nums()
    print(f'{time.ctime()} Goodbye!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)

    for task in pending:
        task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)

    loop.close()