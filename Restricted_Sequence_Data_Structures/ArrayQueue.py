from General_Sequence_Data_Structures.ArraySequence import ArraySequence

class ArrayQueue:
    """A first in, first out sequence of variable length."""

    def __init__(self):
        """Create an empty queue."""
        self.items = ArraySequence()
        self.start = 0

    def enqueue(self, item: object) -> None:
        """Add item to the end of the queue."""
        self.items.append(item)

    def dequeue(self) -> None:
        """Remove the item at the front of the queue.

        Preconditions: the queue isn't empty
        """
        self.items.set_item(self.start, None)   # helps garbage collection
        self.start = self.start + 1

    def front(self) -> object:
        """Return the item at the front of the queue.

        Preconditions: the queue isn't empty
        """
        return self.items.get_item(self.start)

    def __str__(self) -> str:
        """Return a string representation of the queue.

        Postconditions: the string uses Python's list notation
        """
        copy = ArraySequence()
        for index in range(self.start, self.items.length()):
            copy.append(self.items.get_item(index))
        return str(copy)