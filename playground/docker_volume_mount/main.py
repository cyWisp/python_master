import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

if __name__ == '__main__':

    log.info('test')

    log.info(os.getcwd())
    log.info(os.listdir('target'))