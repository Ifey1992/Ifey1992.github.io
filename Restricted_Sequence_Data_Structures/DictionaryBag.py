class Bag:
    """An unordered collection of items, possibly with duplicates.

    Each item must be hashable.
    """

    def __init__(self, items: object):
        """Create a new bag with the given items.

        Preconditions: items is an iterable collection of hashable objects
        """
        self.members = dict()
        for item in items:
            self.add(item)  # you need to implement the add method
            
    def size(self) -> int:
        """
        Return the amount of unique values in the bag (sum of multiplicity of members).
        """
        total_size = 0
        for item in self.members:
            total_size = total_size + self.members[item]
        return total_size
    
    def add(self, item: object) -> None:
        """
        Add an item into the bag and update it's multiplicity.
        """
        if item not in self.members:
            self.members[item] = 1
        else:
            self.members[item] = self.members[item] + 1
    
    def remove(self, item: object) -> None:
        """
        Remove an item from the bag, and updates it's multiplicity. If no item exists in bag, raise error.
        """
        if item not in self.members:
            raise KeyError("No such item")
        if self.members[item] > 1:
            self.members[item] = self.members[item] - 1
        else:
            self.members.pop(item)
        
    def inclusion(self, item: object) -> object:
        """
        Returns True if an item is a member of the bag, otherwise False.
        """
        return item in self.members
    
    def intersection(self, bag: 'Bag') -> 'Bag':
        """
        Return the intersection of two bags (the members in bag1(self) and in bag2(bag))
        """
        new_bag = Bag([]) # an empty bag
        if len(self.members) < len(bag.members): # compares which if the bags in the smallest (fewest unique items)
            (smaller_bag, larger_bag) = self, bag # if self is smaller, assign the smaller_bag to it
        else:
            (smaller_bag, larger_bag) = bag, self # if the parameter bag is smaller, assign smaller_bag to it
        for item in smaller_bag.members: # for each key/member in the smaller_bag
            if item in larger_bag.members: # if this key/member is also in the larger_bag
                min_multi = min(smaller_bag.members[item], larger_bag.members[item]) # compare the bags for the same item and retrieve the lowest multiplicity 
                for times in range (min_multi): # for the number of times equal to the lowest multiplicity
                    new_bag.add(item) # add the item to the new bag
        return new_bag
    
    def union(self, bag: 'Bag') -> 'Bag':
        """
        Return the union of two bags (all items, with the highest multiplicity from either bag).
        """
        new_bag = Bag([]) # an empty bag
        for item, multiplicity in self.members.items(): # add items/multi from first/self bag
            new_bag.members[item] = multiplicity
        for item, multiplicity in bag.members.items():
            if item in new_bag.members: # if the item already exists in the bag
                new_bag.members[item] = max(new_bag.members[item], multiplicity) # update the item to show highest multiplicity
            else: # otherwise, if the item is not in the bag
                new_bag.members[item] = multiplicity
        return new_bag
                
    
    def difference(self, bag: 'Bag') -> 'Bag':
        """
        Return the difference of two bags (items in bag1 not in bag2, with adjusted multiplicity).
        """
        new_bag = Bag([]) # an empty bag
        for item, multiplicity in self.members.items(): # iterate over each key/value pair (member/multiplicity)
            if item not in bag.members: # if the member isnt in the second bag (parameter bag)
                new_bag.members[item] = multiplicity # add the item with it's multiplicity to the new_bag
            else: # otherwise, if the member is in second bag
                # only add if multiplicity in self is greater than in bag
                new_multiplicity = multiplicity - bag.members.get(item, 0) # calculate the difference between multiplicities between first and second bag
                if new_multiplicity > 0: # if the new multiplicity is greater than 0
                    new_bag.members[item] = new_multiplicity # add the item to the new_bag with the updated multiplicity
        return new_bag
                
    def multiplicity(self, item: object) -> int:
        """
        Returns the multiplicity of a member of the bag.
        """
        if item not in self.members:
            raise KeyError("Item does not exist in the bag")
        return self.members[item]
    
    def __str__(self):
        """
        Return a simple readable string representation of the bag.
        """
        items_str = "Bag with items: "
        first = True  # Indicator for the first item
        for item, count in self.members.items():
            if not first:
                items_str += ", "  # Add a separator before all but the first item
            items_str += f"{item}: {count}"
            first = False  # After the first item, this will be False
        return items_str