#!/usr/bin/env python
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

        if key in ('width', 'height'):
            self.__dict__['width'], self.__dict__['height'] = value, value


if __name__ == '__main__':

    new_square = Square(5)
    logging.info(new_square.width)

