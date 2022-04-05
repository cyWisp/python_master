#!/usr/bin/env python
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r},'
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

if __name__ == '__main__':
    p = Pizza(4, ['mozzarella', 'tomatoes'])
    print(p)
    print(p.area())
    print(p.circle_area(4))