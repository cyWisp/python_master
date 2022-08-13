#!/usr/bin/env python

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
    def move(self):
        print(f'{self.species} is moving.')
    
    def eat(self):
        print(f'{self.species} is eating.')
    
    def __str__(self):
        return f'species: {self.species} | age: {self.age}'
    
class Bird(Animal):
    def __init__(self, species, age):
        super().__init__(species, age)

    def fly(self):
        print(f'{self.species} is flying.')

    def eat(self):
        print(f'{self.species} is prodding a meal with its beak')


if __name__ == '__main__':
    new_bird = Bird('toucan', 15)
    new_animal = Animal('dog', 5)

    new_bird.move()
    new_bird.fly()
    new_bird.eat()

    new_animal.move()
    new_animal.eat()