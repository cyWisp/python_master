#!/usr/bin/env python

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f'The {self.make} {self.model} is moving.')

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Airplane(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def fly(self):
        print(f'The {self.make} {self.model} is flying...')

if __name__ == '__main__':
    new_car = Car('ford', 'mustang')
    new_car.move()

    new_airplane = Airplane('boeing', '747')
    new_airplane.move()
    new_airplane.fly()

