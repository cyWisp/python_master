#!/usr/bin/env python
import os
import json
from PIL import Image
import configargparse
import logging

parser = configargparse.get_argument_parser(name='default')
parser.add_argument('--image-dir', type=str, required=False, default='images')
parser.add_argument('--log-level', type=str, required=False, default='INFO')
cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.getLevelName(cfg.log_level)
)

log = logging.getLogger()


class ImageViewer:
    def __init__(self, image_dir: str) -> None:
        self.image_dir = image_dir
        self.images = self.get_dir_contents()
        self.image_paths = self.get_image_paths()
        self.loaded_images = self.load_images()

    def get_dir_contents(self):
        log.debug(f'Getting directory contents for {self.image_dir}')
        return os.listdir(self.image_dir) if os.path.exists(self.image_dir) else None

    def get_image_paths(self):
        log.debug('Building file paths.')
        return [os.path.join(os.path.abspath(self.image_dir), i)
                for i in self.images] if self.images else None

    def load_images(self):
        log.debug('Loading images.')
        loaded = list()

        for image in self.image_paths:
            log.debug(f'Loading {image.split("/")[-1]}')
            with Image.open(image) as img:
                img.load()

            loaded.append(img)
        return loaded

    def show_images(self):
        for i in self.load_images():
            i.show()


if __name__ == '__main__':
    log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

    viewer = ImageViewer(cfg.image_dir)
    viewer.show_images()
