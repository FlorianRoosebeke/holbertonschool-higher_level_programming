#!/usr/bin/python3
"""Iterator wrapper that counts iterations."""
from abc import ABC, abstractmethod


class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterable)
        self.counter += 1
        return item

    def __iter__(self):
        return self
