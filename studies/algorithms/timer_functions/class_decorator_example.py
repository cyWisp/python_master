

class MyClass:
    def __init__(self, value):
        self._value = value

    @staticmethod
    def decorator(func):
        def wrapper(self):
            print("The value before the function call: ", self._value)
            func(self)
            print("The value after the function call: ", self._value)
        return wrapper

    @decorator
    def add(self):
        self._value += 1


if __name__ == '__main__':
    obj = MyClass(5)
    obj.add()
