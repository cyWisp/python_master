#!/usr/bin/env python

class SomeClass:
    class_var_1 = 'this is a class var'

    @classmethod
    def class_method_1(cls):
        return f'Contents of class_var_1: {cls.class_var_1}'

    @classmethod
    def alter_class_state(cls, new_value: str):
        print(f'Updating class var to: {new_value}')
        cls.class_var_1 = new_value


if __name__ == '__main__':
    print(SomeClass.class_method_1())
    SomeClass.alter_class_state('new value')
    print(SomeClass.class_method_1())
