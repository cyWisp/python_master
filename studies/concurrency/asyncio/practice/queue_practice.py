import logging
import asyncio
import random
import sys


logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()
log.name = 'default'


class AsyncNums:
    def __init__(self, qty_nums: int) -> None:
        self.qty_nums = qty_nums
        self.queue = asyncio.Queue()

    async def start(self):
        append_task = asyncio.create_task(self.append_to_queue(), name='Append Task')
        process_task = asyncio.create_task(self.process_queue(), name='Process Task')

        try:
            await asyncio.gather(
                append_task,
                process_task
            )

            await self.queue.join()

        except asyncio.CancelledError as e:
            log.info('Exiting the program')
            sys.exit()

    async def append_to_queue(self):
        log.info(f'{asyncio.current_task().get_name()} starting.')
        log.info(f'Appending {self.qty_nums} to the queue.')

        for i in range(self.qty_nums):
            new_random_number = random.randint(1, 10)
            log.info(f'Random number generated: {new_random_number}')

            await self.queue.put(new_random_number)

        self.queue.task_done()

    @staticmethod
    async def add_five(num: int):
        log.info(f'Adding 5 to {num} | Result: {num + 5}')

    async def process_queue(self):
        log.info(f'{asyncio.current_task().get_name()} starting.')

        while True:
            if self.queue.empty():
                break

            new_number = await self.queue.get()
            log.info(f'Current number: {new_number}')

            await self.add_five(new_number)

        self.queue.task_done()
        raise asyncio.CancelledError



if __name__ == '__main__':
    async_nums = AsyncNums(30)
    asyncio.run(async_nums.start())
