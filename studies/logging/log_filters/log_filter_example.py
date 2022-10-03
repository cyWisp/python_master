import logging
import os


logging.basicConfig(
    format='%(process)d - %(asctime)s - %(some_id)s: %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test.log', 'a+', 'utf-8')
    ]
)



log = logging.getLogger()

for handler in log.handlers:
    handler.addFilter(SystemLogFilter())


if __name__ == '__main__':
    logging.info('this is a basic log info message.')
    logging.info('this message has some id', extra={'some_id': '112233445566'})

