#!/usr/bin/env python

class Animal:
    def __init__(self, name, color):
        self.name, self.color = name, color

    def walk(self):
        print(f'The {self.color} {self.name} is walking.')

    def run(self):
        print(f'The {self.color} {self.name} is running.')


class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def fly(self):
        print(f'The {self.color} {self.name} is flying.')


class Monkey(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def swing(self):
        print(f'The {self.color} {self.name} is swinging.')


if __name__ == '__main__':
    new_bird = Bird('parrot', 'green')
    new_monkey = Monkey('orangutan', 'brown')

    new_bird.walk()
    new_bird.fly()

    new_monkey.walk()
    new_monkey.swing()