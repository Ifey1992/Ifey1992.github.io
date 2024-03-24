class HashMap:
    """An unordered collection of key-value pairs.

    Keys must be unique and hashable.
    """

    # The hash table is a dynamic array of slots.
    # Each slot is a dynamic array of key-value pairs.

    def __init__(self):
        self.slots = [ [] ]     # start with 1 slot
        self.size = 0

    def has(self, key: object) -> bool:
        """Return True if and only if key is in the map.

        Preconditions: key is hashable
        """
        index = hash(key) % len(self.slots)
        slot = self.slots[index]
        # linear search of the key in the only slot it can be
        for pair in slot:
            if pair[0] == key:
                return True
        return False

    def grow(self) -> None:
        """Grow the dictionary if necessary.

        Postconditions:
        if pre-self has load factor 1, post-self has load factor 0.5
        """
        capacity = len(self.slots)
        if self.size == capacity:
            # new hash table with double the slots, all empty
            new_capacity = capacity * 2
            new_slots = []
            for each_slot in range(new_capacity):
                new_slots.append([])
            # put each pair in the correct slot in the new table
            for slot in self.slots:
                for pair in slot:
                    index = hash(pair[0]) % new_capacity
                    new_slots[index].append(pair)
            # use the new hash table
            self.slots = new_slots

    def associate(self, key: object, value: object) -> None:
        """Associate value to key in the map.

        Preconditions: key is hashable
        Postconditions: looking up key in self returns value
        """
        self.grow()
        index = hash(key) % len(self.slots)
        slot = self.slots[index]
        for pair in slot:
            if pair[0] == key:
                pair[1] = value
                return
        slot.append( [key, value] )
        self.size = self.size + 1