class LinkedDeque:
    """A doubly linked list implementation of the deque ADT."""

    class Node:
        """An individual node in a doubly linked list."""
        def __init__(self, item):
            """Create an unchained node with the item."""
            self.item = item
            self.previous = None
            self.next = None

    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = []
        current = self.head
        while current != None:
            items.append(current.item)
            current = current.next
        return str(items)

    def front(self) -> object:
        return self.head.item

    def back(self) -> object:
        return self.end.item

    def append(self, item: object) -> None:
        new = LinkedDeque.Node(item)    # no previous/next node
        if self.head == None:   # empty deque
            self.head = new
            self.end = new
        else:                   # there's a last node: self.end
            self.end.next = new
            new.previous = self.end
            self.end = new
        self.size = self.size + 1

    def prepend(self, item: object) -> None:
        new = LinkedDeque.Node(item)
        if self.head == None:
            self.head = new
            self.end = new
        else:
            new.next = self.head
            self.head.previous = new
            self.head = new
        self.size = self.size + 1
   
    def remove_front(self) -> None:
        self.head = self.head.next
        if self.head == None:           # deque is now empty
            self.end = None
        else:                           # update new head node
            self.head.previous = None
        self.size = self.size - 1

    def remove_back(self) -> None:
        """Remove an item from the end of the deque"""
        if self.head == self.end:
            self.head = None
            self.end = None
        else:
            self.end = self.end.previous
            self.end.next = None
        self.size = self.size -1 