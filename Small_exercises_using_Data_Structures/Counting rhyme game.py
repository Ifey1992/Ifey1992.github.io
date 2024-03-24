#Given the number of children n, we want to know the number of the last remaining child

from collections import deque

def counting_rhyme(n: int) -> int:
    children = deque()
    for child in range(1, n+1):
        children.append(child)
    for round in range(n-1):
        for syllable in range(27):
            children.append(children.popleft())
        children.popleft()
    return children[0]

# Tests

counting_rhyme_tests = [
    # case,         n,  last child
    ['1 child',     1,          1],
    ['2 children',  2,          1],
    ['3 children',  3,          2]
]
