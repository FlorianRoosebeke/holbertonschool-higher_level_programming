#!/usr/bin/python3
"""Basic ABC example with animals and sounds."""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return ("Berk")


class Cat(Animal):
    def sound(self):
        return ("Meow")


bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())
