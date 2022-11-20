#!/usr/bin/env python
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.DEBUG,
)

log = logging.getLogger()

if __name__ == '__main__':
    from unsplash_images import image_downloader

    image_downloader = image_downloader.ImageDownloader(['breasts', 'boobs', 'sex', 'vixen'])
