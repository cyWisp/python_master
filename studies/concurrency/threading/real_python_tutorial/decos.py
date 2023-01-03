#/usr/bin/env python
import concurrent.futures
import functools
import logging
import time


logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger()


def timer(log):
    def deco(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)

            run_time = time.perf_counter() - start_time
            log.info(f"Finished {func.__name__!r} - {kwargs['thread_id']} - Runtime: {run_time:.4f} secs")
            return value
        return wrapper_timer
    return deco


@timer(log)
def log_things(name):
    log.info(f'Starting thread {name}.')
    time.sleep(2)
    log.info(f'Finishing thread {name}')

    return name


if __name__ == '__main__':
    num_workers = 5

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as ex:
        for i in range(num_workers):
            ex.submit(log_things, i)

