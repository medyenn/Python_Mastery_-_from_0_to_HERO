# Abstraction concept focuses on showing the results while hiding the
# the process and unnecessary info and steps from the user.
# So we only care about the outcome without digging into implementation details

# For Python it doesn' support abstraction by default, but we still can get
# abstraction in python using the Abstractin Base Classes (abc) Module
# by importing ABC from abc module

# Abstract Class:

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):
        ...

    def breath(self):
        print('I can breath !')


class Human(Creature):
    def __init__(self, name='human'):
        super().__init__(name)

    def eat(self):
        print('I eat meat and plants !')


class Herbivore(Creature):
    def __init__(self, name='animal', breed='cow'):
        super().__init__(name)
        self.breed = breed

    def eat(self):
        print('I only eat plants !')


class Carnivore(Creature):
    def __init__(self, name='animal', breed='dog'):
        super().__init__(name)
        self.breed = breed

    def eat(self):
        print('I only eat meat !')


# c = Creature()
human = Human('Jey')
