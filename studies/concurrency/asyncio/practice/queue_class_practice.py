import logging
import asyncio
import random


logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')
log = logging.getLogger()


class ProcessRandom:
    def __init__(
        self,
        qty: int,
        min_max: tuple
    ):
        self.qty, self.min_max = qty, min_max
        self.queue = asyncio.Queue()
        self.results = []

    async def generate_random_number(self):
        for n in range(self.qty):
            log.debug(f'Generating random number ->')
            new_random_number = random.randint(self.min_max[0], self.min_max[1])

            log.debug(new_random_number)
            await self.queue.put(new_random_number)
            await asyncio.sleep(0)

    @staticmethod
    async def add_five(num: int):
        log.debug(f'Performing addition.')
        return num + 5

    async def process_queue(self):
        while True:


            num = await self.queue.get()

            result = await self.add_five(num)

            log.debug(f'{num} + 5 = {result}')
            self.results.append(result)
            self.queue.task_done()

    async def main(self):
        log.debug('Init main.')

        generate_task = asyncio.create_task(self.generate_random_number())
        process_task = asyncio.create_task(self.process_queue())

        await asyncio.gather(generate_task, process_task)
        await self.queue.join()

        log.debug('Task completed!')


if __name__ == '__main__':
    proc_object = ProcessRandom(10, (1, 10))
    asyncio.run(proc_object.main())

    log.info(proc_object.results)
