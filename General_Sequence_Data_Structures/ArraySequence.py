from StaticArray import StaticArray
from PartialSequenceADT import Sequence
from DynamicArray import DynamicArray

import math

class ArraySequence(Sequence):
    """A dynamic array implementation of the sequence ADT."""

    def __init__(self):
        """Create an empty sequence."""
        self.items = DynamicArray(1)
        self.size = 0

    def capacity(self) -> float:
        return math.inf     # infinite capacity

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        if self.size == self.items.length():    # array full
            self.items.resize(2 * self.size)    # double the capacity

        for position in range(self.size - 1, index - 1, -1):
            self.set_item(position + 1, self.get_item(position)) # shift items up a position 
        self.items.set_item(index, item) # insert item at given index
        self.size = self.size + 1
        
    def remove(self, index: int) -> None:
        for position in range(index + 1, self.size):
            self.items.set_item(position -1, self.items.get_item(position))
        self.size = self.size - 1
        
        if self.size < self.items.length() // 2:
            new_cap = max(1, self.items.length() // 2)
            self.items.resize(new_cap)