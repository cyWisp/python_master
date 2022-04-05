#!/usr/bin/env python

# Note: 'self' denotes instance

class MyClass:
    class_var = 'this is a class var'

    # Instance method
    def method(self):
        return 'instance method called', self

    # Instance method editing class state
    def change_class_state(self):
        self.__class__.class_var = 'changed'

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

if __name__ == '__main__':
    # Instance method example ============================
    obj = MyClass()

    # These calls will product the same result
    print(obj.method())

    # This proves that the argument the method accepts is
    # an instance of the MyClass() object.
    print(MyClass.method(obj))

    MyClass.change_class_state(obj)
    print(MyClass.class_var)
    # ===================================================