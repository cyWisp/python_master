#!/usr/bin/env python
import logging
import json
import sys

from config import parser


cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[
        logging.FileHandler(cfg.log_file, 'a+', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger()

log.debug(json.dumps(vars(cfg), indent=4))

if __name__ == '__main__':
    from db.ms_api import MSInterface

    ms_db = MSInterface(
        'comic_book_shop_1',
        'localhost',
        'root',
        'password'
    )

    ten_invoices = ms_db.execute_query('SELECT * FROM invoices LIMIT 1, 10')
    log.info(json.dumps(ten_invoices, indent=4))
