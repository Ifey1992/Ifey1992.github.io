from StaticArray import StaticArray
from PartialSequenceADT import Sequence

class BoundedSequence(Sequence):
    """A sequence with a fixed capacity."""

    def __init__(self, capacity: int):
        """Create an empty sequence that can hold 'capacity' items.

        Preconditions: capacity >= 0
        """
        self.items = StaticArray(capacity)
        self.size = 0

    def capacity(self) -> int:
        return self.items.length()

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        for position in range(self.size-1, index-1, -1):
            self.items.set_item(position + 1, self.items.get_item(position))
        self.items.set_item(index, item)
        self.size = self.size + 1
    
    def remove(self, index: int) -> None:
        for position in range(index + 1, self.size):
            self.items.set_item(position - 1, self.items.get_item(position)),
        self.size = self.size - 1