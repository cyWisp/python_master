import random


class Module1:
    def __init__(self):
        pass

    @staticmethod
    def add(value_1, value_2):
        return value_1 + value_2

    @staticmethod
    def sub(value_1, value_2):
        return value_1 - value_2

    @staticmethod
    def mult(value_1, value_2):
        return value_1 * value_2


class RandomStuff:
    @staticmethod
    def generate_random_numbers(qty: int) -> list:
        return [random.randint(1, qty) for x in range(qty)]

