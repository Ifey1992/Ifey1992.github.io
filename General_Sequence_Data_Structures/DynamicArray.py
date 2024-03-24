from StaticArray import StaticArray

class DynamicArray(StaticArray):
    """An array that can grow and shrink."""

    def resize(self, length: int) -> None:
        """Shorten or extend the array to the new length.

        Preconditions: 0 <= length; length != self.length()
        Postconditions: if pre-self is a_0, a_1, ..., a_n then
        post-self is b_0, b_1, ..., b_m with
        - n == pre-self.length() - 1
        - m == length - 1
        - b_i == a_i for every i from 0 to min(n, m)
        - b_i == None for every i from min(m, n) + 1 to m
        """
        new_array = [None] * length
        for index in range(0, min(length, self.length())):
            new_array[index] = self.items[index]
        self.items = new_array