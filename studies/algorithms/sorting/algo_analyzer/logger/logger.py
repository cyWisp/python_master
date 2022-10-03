import logging
import sys


def setup_logging(log_level: str, log_file: str) -> logging.Logger:
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.getLevelName(log_level.upper()),
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, 'a+', 'utf-8')
        ]
    )
    log = logging.getLogger()

    return log