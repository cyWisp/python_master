#!/usr/bin/env python

class Tail:
    def __init__(self):
        self.length = None
        self.texture = None

    def set_length(self, length):
        self.length = length

    def set_texture(self, texture):
        self.texture = texture

    def get_length(self):
        return self.length

    def get_texture(self):
        return self.texture

    def __str__(self):
        return f'Length: {self.length} | Texture: {self.texture}'


class Animal:
    def __init__(self, species, color):
        self.species, self.color = species, color
        self.tail = Tail()

    def move(self):
        print(f'The {self.color} {self.species} is moving.')

    def eat(self):
        print(f'The {self.color} {self.species} is eating.')


class Dog(Animal):
    def __init__(self, species, color, breed):
        super().__init__(species, color)
        self.breed = breed

    def bark(self):
        print(f'The {self.color} {self.breed} {self.species} is barking...')

    def wag(self):
        print(f'The {self.color} {self.breed} {self.species} is wagging its {self.tail.length} {self.tail.texture} tail.')

if __name__ == '__main__':
    labrador = Dog('canine', 'black', 'labrador')
    labrador.bark()

    labrador.tail.set_length('long')
    labrador.tail.set_texture('furry')

    labrador.move()

    labrador.wag()

    labrador.eat()