class StaticArray:
    """A fixed-length sequence of references in contiguous memory."""

    def __init__(self, length: int):
        """Create an array of the given length.

        Preconditions: length >= 0
        Postconditions: every item in the array is None
        """
        # assume lists are stored in arrays
        self.items = [None] * length

    def length(self) -> int:
        """Return the length of the array."""
        return len(self.items)

    def get_item(self, index: int) -> object:
        """Return the item at the given index.

        Preconditions: 0 <= index < self.length()
        """
        return self.items[index]

    def set_item(self, index: int, item: object) -> None:
        """Replace the item at the given index with the given item.

        Preconditions: 0 <= index < self.length()
        Postconditions: self.get_item(index) == item
        """
        self.items[index] = item

    def __str__(self) -> str:
        """Return a string representation of the array."""
        return str(self.items)
    
    # Test the StaticArray class (comment out)
# array = StaticArray(5)  # Create an array of length 5
# print(array)  # Print the initial array

# array.set_item(0, "Hello")
# array.set_item(1, "World")
# print(array.get_item(0))  # Should print "Hello"
# print(array)  # Print the array after setting items

# print("Length of array:", array.length())  # Print the length of the array