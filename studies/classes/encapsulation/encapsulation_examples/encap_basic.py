import json

class Example:
    def __init__(self):
        self.__private_var = 'this is a private var'

    def __private_method(self):
        print('This is a private method.')
        print(self.__private_var)

    def _protected_method(self):
        print('This is a quazi private method.')

    def public_method(self):
        self.__private_method()


if __name__ == "__main__":
    example = Example()

    example.public_method()
    example._protected_method()