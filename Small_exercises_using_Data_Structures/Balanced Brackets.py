# Given a string, containing Python code or some other text, we want to know if the brackets within that string are balanced

"""
Step-bystep algorithm:

let opened be an empty stack
for each character in text:
    if character = '(' or character = '[':
        push character on opened
    otherwise if character = ')':
        if │opened│ > 0 and top of opened = '(':
            pop opened
        otherwise:
            let balanced be false
            stop
    otherwise if character = ']':
        if │opened│ > 0 and top of opened = '[':
            pop opened
        otherwise:
            let balanced be false
            stop
let balanced be │opened│ = 0
"""

def balanced(exp: str) -> bool:
    brackets = [] # a stack
    for char in exp:
        if char == "(" or char == "[":
            brackets.append(char)
        elif char == ")":
            if len(brackets) > 0 and brackets[-1] == "(":
                brackets.pop()
            else:
                return False
        elif char == "]":
            if len(brackets) > 0 and brackets[-1] == "[":
                brackets.pop()
            else:
                return False
    return len(brackets) == 0

# Tests

is_balanced_tests = [
    # case,         text,                               balanced
    ['no text',     '',                                 True],
    ['no brackets', 'brackets are like Russian dolls',  True],
    ['matched',     '(3 + 4)',                          True],
    ['mismatched',  '(3 + 4]',                          False],
    ['not opened',  '3 + 4]',                           False],
    ['not closed',  '(3 + 4',                           False],
    ['wrong order', 'close ) before open (',            False],
    ['nested',      '([([])])',                         True],
    ['nested pair', 'items[(i - 1):(i + 1)]',           True]
]