#!/usr/bin/env python

class Dog():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking loudly...")

def get_oldest(dog_list):
    for d in dog_list:
        if not d:
            break
        else:
            highest = d.age
            name = d.name
            if d.age > highest:
                highest = d.age
                name = d.name
            else:
                pass
    return name, highest

if __name__ == '__main__':
    dogs = {'mickey': 2, 'spot': 5, 'timmy':6}
    new_dogs = list()

    for k, v in dogs.items():
        new_dog = Dog(k, v)
        new_dogs.append(new_dog)

    name, oldest = get_oldest(new_dogs)
    print(f"Oldest dog: {name}, Age: {oldest}")

        