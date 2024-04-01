import asyncio
import logging
from uuid import uuid4
from random import randint

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()
log.name = 'default'


async def print_10_numbers():
    log.info(f'{asyncio.current_task().get_name()} starting.')

    for i in range(10):
        if i == 5:
            await asyncio.sleep(1)

        log.info(i)


async def print_10_letters():
    log.info(f'{asyncio.current_task().get_name()} starting.')

    for i in range(10):
        if i == 5:
            await asyncio.sleep(1)

        log.info(chr(randint(65, 90)))


async def main():
    numbers_task = asyncio.create_task(print_10_numbers(), name='Numbers task')
    letters_task = asyncio.create_task(print_10_letters(), name='Letters task')

    await asyncio.gather(numbers_task, letters_task)

if __name__ == '__main__':
    log.info('Creating Tasks.')
    asyncio.run(main())