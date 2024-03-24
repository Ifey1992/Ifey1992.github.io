class Sequence:
    """The sequence ADT."""

    def capacity(self) -> float:
        """Return how many items the sequence can hold.

        Postconditions: if the capacity is only limited by memory,
        the output is math.inf,
        otherwise it's the non-negative integer set at creation time
        """
        pass

    def length(self) -> int:
        """Return the number of items in the sequence.

        Postconditions: 0 <= self.length() <= self.capacity()
        """
        pass

    def get_item(self, index: int) -> object:
        """Return the item at position index.

        Preconditions: 0 <= index < self.length()
        Postconditions: the output is the n-th item of self, with n = index + 1
        """
        pass

    def set_item(self, index: int, item: object) -> None:
        """Replace the item at position index with the given one.

        Preconditions: 0 <= index < self.length()
        Postconditions: post-self.get_item(index) == item
        """
        pass

    def insert(self, index: int, item: object) -> None:
        """Insert item at position index.

        Preconditions: 0 <= index <= self.length() < self.capacity()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(index - 1),
        item, pre-self.get_item(index), ...,
        pre-self.get_item(pre-self.length() - 1)
        """
        pass

    def append(self, item: object) -> None:
        """Add item to the end of the sequence.

        Preconditions: self.length() < self.capacity()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(pre-self.length() - 1), item
        """
        self.insert(self.length(), item)

    def remove(self, index: int) -> None:
        """Remove the item at the given index.

        Preconditions: 0 <= index < self.length()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(index - 1),
        pre-self.get_item(index + 1), ...,
        pre-self.get_item(pre-self.length() - 1)
        """
        pass    

    def has(self, item: object) -> bool:
        """Return True if and only if item is a member of self """
        for index in range(self.length()):
            if self.get_item(index) == item:
                return True
        return False

    def __str__(self) -> str:
        """Return a string representation of the sequence.

        Postconditions: the output uses Python's syntax for lists
        """
        items = []
        for index in range(self.length()):
            items.append(self.get_item(index))
        return str(items)