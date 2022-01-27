#!/usr/bin/env python
import asyncio
import json

async def f():
    print('this is the inner function')
    await asyncio.sleep(1)
    return "f()'s return value"

async def g():
    print('this is the outer function')
    print('waiting on f()')
    f_ret = await f()
    print(f'all done... | f() returned {f_ret}')

async def main():
    await asyncio.gather(g(), f())


if __name__ == '__main__':
    asyncio.run(main())
    print("this is outside the coroutines")