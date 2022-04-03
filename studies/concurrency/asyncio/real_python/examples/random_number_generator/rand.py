#!/usr/bin/env python
import asyncio
import random

# ANSI colors
color = (
    "\033[0m",  # End of Color
    "\033[36m", # Cyan
    "\033[91m", # Red
    "\033[35m"  # Magenta
)

async def make_random(index: int, threshold: int = 6) -> int:
    print(color[index + 1] + f"Initiated make_random({index})")
    random_int = random.randint(0, 10)

    # while random int is less than or equal to threshold
    while random_int <= threshold:
        print(color[index + 1] + f"make_random({index}) == {random_int} too low; retrying.")
        await asyncio.sleep(index + 1)
        random_int = random.randint(0, 10)

    print(color[index + 1] + f"---> Finished: make_random({index}) == {random_int}{color[0]}")
    return random_int

async def main():
    result = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return result

if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f'\nresult 1: {r1} | result 2: {r2} | result 3: {r3}')
