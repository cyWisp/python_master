#!/usr/bin/env python
import logging

from abc import ABC, abstractmethod
from math import pi


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__('rectangle')
        self.length, self.width = length, width

    def calculate_area(self):
        return self.length * self.width


class Square(Shape):
    def __init__(self, side):
        super().__init__('square')
        self.side = side

    def calculate_area(self):
        return self.side**2


if __name__ == '__main__':
    new_circle = Circle(3)
    new_rect = Rectangle(3, 4)
    new_square = Square(5)

    log.info(f'Circle Shape Type: {new_circle.shape_type}')
    log.info(f'Rectangle Shape Type: {new_rect.shape_type}')
    log.info(f'Square Shape Type: {new_square.shape_type}')

    log.info(f'Circle Area: {new_circle.calculate_area()}')
    log.info(f'Rectangle Area: {new_rect.calculate_area()}')
    log.info(f'Square Area: {new_square.calculate_area()}')
