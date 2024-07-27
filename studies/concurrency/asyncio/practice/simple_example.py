import asyncio
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


async def greet(name: str = 'Rob'):
    log.info(f'Starting {asyncio.current_task().get_name()}')
    await asyncio.sleep(1)
    log.info(f'Hi {name}')


async def func_2():
    log.info(f'Starting {asyncio.current_task().get_name()}')
    await asyncio.sleep(1)
    log.info('func_2 finished')


async def main():
    task_1 = asyncio.create_task(greet(), name='Greeter task')
    task_2 = asyncio.create_task(func_2(), name='Task 2')

    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    asyncio.run(main())
