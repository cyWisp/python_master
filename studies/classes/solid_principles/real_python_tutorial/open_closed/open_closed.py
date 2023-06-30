#!/usr/bin/env python
from math import pi


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type

        if self.shape_type == 'rectangle':
            self.width = kwargs.get('width')
            self.height = kwargs.get('height')

        if self.shape_type == 'circle':
            self.radius = kwargs.get('radius')

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self.width * self.height

        if self.shape_type == 'circle':
            return pi * self.radius**2


if __name__ == '__main__':

    new_circle = Shape('circle', radius=3)

    print(new_circle.calculate_area())
