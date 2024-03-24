from StackADT import Stack

class BoundedStack(Stack):
    
    def __init__(self, capacity: int):
        self.items = [] # a stack
        self.size = 0 # keep track of size of stack
        self.capacity = capacity # ensure the size doesn't grow past capacity
    
    def get_size(self) -> int:
        return self.size # returns the size of the Stack
    
    def push(self, value: object) -> None:
        if self.size < self.capacity: # if the size of the stack is less than the capacity
            self.items.append(value) # append the given param value to the items list
            self.size = self.size + 1 # increment the size of the stack as just added an element
        else:
            return "Capacity reached" # if size is not less that capacity, limit has been reached and cannot add more
        
    def pop(self) -> object:
        if self.size == 0: # if the size of the stack is equal to zero (empty list), return its empty
            return "Empty Stack"
        else:
            remove_item = self.items[-1] # remove item var refers to the last item in the items list/stack
            self.items = self.items[:-1] # stack is now a slice from beginning, until second to last element as 2nd arguement is exlusive
            self.size = self.size - 1 # decrement the size of the stack as item has been removed
            return remove_item # return the element thats just been removed
    
    def peek(self) -> object:
        if self.size == 0: # if the size of the stack is zero, or empty.
            return "Empty Stack" # return exactly this, that it's empty
        return self.items[-1] # if not empty, returns the last element of the stack
    
    def __str__(self):
        return str(self.items) # print method, though not exactly needed when we have access to .items
    
    
"""
Black-box testing - comment out
def check(case: str, actual: object, expected: object, context: object) -> None:
    if actual != expected:
        print(case, 'FAILED for', context, ':', actual, 'instead of', expected)

def test_push(capacity: int) -> None:
    new_stack = BoundedStack(capacity)
    for index in range(capacity):
        new_stack.push(index)
        check("Test pushing item on top of stack", new_stack.peek(), index, new_stack)

def test_pop(capacity: int) -> None:
    new_stack = BoundedStack(capacity)
    for index in range(capacity):
        new_stack.push(index)
    for index in range(capacity-1, -1, -1):
        check('Test removed', new_stack.pop(), index, new_stack)

def test_peek(capacity: int) -> object:
    new_stack = BoundedStack(capacity)
    for index in range(capacity):
        new_stack.push(index)
        check("Test to check top item of stack", new_stack.peek(), index, new_stack)
Operation"""