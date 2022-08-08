#!/usr/bin/env python
import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://cybersherpa.net') as response:

            print(f"Status: {response.status}")
            print(f"Content-type: {response.headers['content-type']}")

            html = await response.text()
            print(f"Body: {html[:15]}...")

if __name__ == '__main__':
    asyncio.run(main())