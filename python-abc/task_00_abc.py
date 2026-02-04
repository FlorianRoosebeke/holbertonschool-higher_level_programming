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
