from modules.module_1 import Module1
from modules.module_1 import RandomStuff


class TestOps:

    def test_addition(self):
        assert Module1.add(1, 2) == 3, 'Addition failed.'

    def test_subtraction(self):
        assert Module1.sub(2, 1) == 1, 'Subtraction failed.'

    def test_multiplication(self):
        assert Module1.mult(2, 1) == 1, 'Multiplication failed.'

    def test_rng(self):
        random_numbers = RandomStuff.generate_random_numbers(20)

        assert isinstance(random_numbers, list), 'Not a list'
        assert len(random_numbers) == 20, 'Incorrect quantity.'
