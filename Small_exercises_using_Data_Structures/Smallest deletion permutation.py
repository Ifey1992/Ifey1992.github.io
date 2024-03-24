# Given two sequences of items, what is the smallest number of items to be removed from both sequences so that one becomes a permutation

from collections import Counter

def deletions(left: list, right: list) -> int:
    """Return how many deletions make the lists have the same items.

    Postconditions:
    - the output is the smallest number of deletions necessary
    """
    left_count = Counter(left)
    right_count = Counter(right)
    deleted = (left_count | right_count) - (left_count & right_count)
    count = 0
    for (key, value) in deleted.items():
        count = count + value
    return count
    
deletions_tests = [
    # case,             left,                   right,  deletions
    ('some overlap',    [1, 2, 3, 2],           [3, 2, 2, 5],   2),
    ('one common',      ['a','man','a','plan'], ['a','canal'],  4),
    ('random',          [1, 2, 2, 2, 4],        [1, 2, 3, 4], 3)
    # new tests
]