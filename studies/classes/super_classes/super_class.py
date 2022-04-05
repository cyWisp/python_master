#!/usr/bin/env python

class SuperClass:
    str_class_var = 'some string'
    list_class_var = ['first value', 'second value']

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.info_list = [self.name, self.age, self.location]

    def __repr__(self):
        return f'SuperClass({self.info_list})'

    @classmethod
    def get_class_vars(cls):
        return [cls.str_class_var, cls.list_class_var]

class SubClass(SuperClass):
    def __init__(self, name, age, location):
        super().__init__(name, age, location)


if __name__ == '__main__':
    new_sub = SubClass('rob', 36, 'Miami')
    print(new_sub)
    print(new_sub.get_class_vars())
    print(new_sub.info_list)

