#!/usr/bin/env python

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'tomatoes'])

    @classmethod
    def proscuitto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])

if __name__ == '__main__':
    new_pizza = Pizza.margherita()
    print(new_pizza.ingredients)
