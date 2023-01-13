import functools
import time


def timer(log):
    def deco(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            func(*args, **kwargs)

            run_time = time.perf_counter() - start_time
            log.info(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return wrapper_timer
    return deco


def async_timer(log):
    def deco(func):
        @functools.wraps(func)
        async def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            await func(*args, **kwargs)

            run_time = time.perf_counter() - start_time
            log.info(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return wrapper_timer
    return deco