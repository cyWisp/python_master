#!/usr/bin/env python

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Warrior(Person):
    def __init__(self, attack_power, defense_power):
        self.attack_power = attack_power
        self.defense_power = defense_power
    def description(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAttack: {self.attack_power}\nDefense: {self.defense_power}")

if __name__ == '__main__':
    warrior_1 = Warrior(12, 12)

    warrior_1.description()