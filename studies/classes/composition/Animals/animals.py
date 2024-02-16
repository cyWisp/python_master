import logging
from abc import ABC, abstractmethod

log = logging.getLogger()


class Animal(ABC):
    def __init__(
        self,
        name: str,
        color: str
    ):
        self.name, self.color = name, color

    def __str__(self):
        return vars(self)

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def __init__(
        self,
        name: str,
        color: str,
        breed: str,
        owner: str
    ):
        super().__init__(name, color)
        self.breed, self. owner = breed, owner

    def move(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is running around.')

    def eat(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is eating.')

    def play_ball(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is playing ball'
                 f' with his owner {self.owner}')


class Birb(Animal):
    def __init__(
        self,
        name: str,
        color: str,
        flight_pattern: str,
        owner: str
    ):
        super().__init__(name, color)
        self.breed, self. owner = breed, owner

    def move(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is running around.')

    def eat(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is eating.')

    def play_ball(self):
        log.info(f'The {self.color} {self.breed} named {self.name} is playing ball'
                 f' with his owner {self.owner}')