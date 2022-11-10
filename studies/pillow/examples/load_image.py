#!/usr/bin/env python
from PIL import Image
import logging

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.INFO,
)

log = logging.getLogger()

if __name__ == '__main__':
    file_name = 'images/buildings.jpg'

    log.info(f'Loading {file_name}.')

    with Image.open(file_name) as img:
        img.load()

    log.info(f'Image: {type(img)} | {isinstance(img, Image.Image)}')

    log.info('Opening image with image viewer...')
    img.show()