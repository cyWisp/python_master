import logging
import asyncio
import random

logging.basicConfig(format='%(funcName)s: %(message)s', level=logging.DEBUG)
log = logging.getLogger()


class ProcessRandom:
    def __init__(
        self,
        num_random: int,
        min_max_values: tuple
    ):
        self.num_random = num_random
        self.min_max_values = min_max_values

        self.queue = asyncio.Queue()
        self.results = []

    async def generate_random_numbers(self):
        for _ in range(self.num_random):
            new_q_item = random.randint(self.min_max_values[0], self.min_max_values[1])

            log.debug(f'Appending {new_q_item} to queue.')
            await self.queue.put(new_q_item)
            await asyncio.sleep(0)

    @staticmethod
    async def add_five(num: int):
        return num + 5

    async def process_queue(self):
        while True:
            if len(self.results) == self.num_random and self.queue.empty():
                log.info('Processing complete.')
                break

            q_item = await self.queue.get()

            log.info(f'Processing {q_item}.')
            operation_result = await self.add_five(q_item)

            log.info(f'Operation: {q_item} + 5 = {operation_result}')
            self.results.append(operation_result)
            self.queue.task_done()

    async def run(self):
        generate_tasks = asyncio.create_task(self.generate_random_numbers())
        process_tasks = asyncio.create_task(self.process_queue())

        await asyncio.gather(generate_tasks, process_tasks)
        await self.queue.join()

        log.info('Back in run function')


if __name__ == '__main__':
    random_number_processor = ProcessRandom(50, (1, 50))
    asyncio.run(random_number_processor.run())
