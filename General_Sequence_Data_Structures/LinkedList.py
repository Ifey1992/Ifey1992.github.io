from PartialSequenceADT import Sequence

import math

class LinkedSequence(Sequence):
    """A linked list implementation of the sequence ADT."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the sequence to be empty."""
        self.head = None

    def capacity(self) -> float:
        return math.inf     # infinite capacity

    def length(self) -> int:
        size = 0
        current = self.head
        while current != None:
            size = size + 1
            current = current.next
        return size

    def get_item(self, index: int) -> object:
        current = self.head
        for times in range(index):
            current = current.next
        return current.item

    def set_item(self, index: int, item: object) -> None:
        current = self.head
        for times in range(index):
            current = current.next
        current.item = item

    def insert(self, index: int, item: object) -> None:
        new = LinkedSequence.Node(item)
        if index == 0:
            new.next = self.head
            self.head = new
        else:
            before = self.head
            for times in range(index - 1):
                before = before.next
            new.next = before.next
            before.next = new
            
    def remove(self, index:int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for index in range(index -1):
                current = current.next
            current.next = current.next.next