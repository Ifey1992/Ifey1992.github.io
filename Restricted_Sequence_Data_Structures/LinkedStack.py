class LinkedStack:
    """A last-in, first-out sequence of objects."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the stack to be empty."""
        self.head = None
        self.length = 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return self.length

    def peek(self) -> object:
        """Return the top item in the stack.

        Preconditions: self.size() > 0
        """
        return self.head.item

    def pop(self) -> None:
        """Remove the top item from the stack.

        Preconditions: self.length() > 0
        """
        self.head = self.head.next
        self.length = self.length - 1

    def push(self, item: object) -> None:
        """Put the given item on top of the stack.

        Postconditions: post-self.peek() == item
        """
        new = LinkedStack.Node(item)
        new.next = self.head
        self.head = new
        self.length = self.length + 1