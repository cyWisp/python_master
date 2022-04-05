#!/usr/bin/env python

class Example:
    class_var_name = 'Rob'
    def __init__(self):
        self.instance_var_name = 'Sam'

    @classmethod
    def change_class_var_name(cls, new_name):
        cls.class_var_name = new_name

    # instance method
    def change_instance_var_name(self, new_name):
        self.instance_var_name = new_name

if __name__ == '__main__':
    new_example = Example()
    print(f'Class var name: {new_example.class_var_name}')
    print(f'Instance var name: {new_example.instance_var_name}')

    print('changing class var to "bill" with class method')
    Example.change_class_var_name('bill')

    print(f'new_example class var: {new_example.class_var_name}')