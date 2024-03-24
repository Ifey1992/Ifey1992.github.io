class Stack:
    """An implementation of the Stack ADT"""
    
    def size(self) -> int:
        """
        Retun the number of items in the Stack.
        
        Postconditions: 0 <= self.length() <= self.capacity()
        """
        pass
    
    
    def push(self, value: object) -> None:
        """
        Insert a value on top of the Stack.
        
        Post-conditions: post-values = pre-values(pre-values[0]... pre-values[│pre-values│-1], value)
        """
        pass
    
    
    def pop(self) -> None:
        """
        Remove the value at the highest index/last element of the list.
        
        Pre-conditions: 0 < │values│ - the length of values (the Stack) must be greater than 0.
        Post-conditions: post-values = (pre-values[0], ..., pre-values[pre-values − 2]) - new item is one less than the 
        last index.
        """
        pass
    
    
    def peak(self) -> object:
        """
        Access the top item of the stack (the highest index/last element).
        
        Preconditions: 0 < │values│ - the length of values (the Stack) must be greater than 0.
        Postconditions: value is the n-th item of values, with n = │values│ - nth meaning final index/element of list.
        """
        pass