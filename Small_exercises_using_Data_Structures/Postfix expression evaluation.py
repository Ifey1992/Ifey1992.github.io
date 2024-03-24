# Outline an algorithm that evaluates a postfix expression, given as a non-empty sequence of characters '−' and '*' and natural numbers

def evaluate(expression: str) -> int:
    operands = [] # a implentation of a stack
    for item in expression:
        if item == "-":
            right = operands.pop()
            left = operands.pop()
            operands.append(left - right)
        elif item == "*":
            right = operands.pop()
            left = operands.pop()
            operands.append(left * right)
        else:
            operands.append(item)
    return operands[-1]

# Tests

evaluate_tests = [
    # case,             expression,                     value
    ['3 * 4',           [3, 4, '*'],                    12],
    ['3 - 4',           [3, 4, '-'],                    -1],
    ['3 - 4 * 5',       [3, 4, 5, '*', '-'],            -17],
    ['(3 - 4) * 5',     [3, 4, '-', 5, '*'],            -5],
    ['(3 - 4) * (5 - 6)', [3, 4, '-', 5, 6, '-', '*'],  1],
    ['no operation',    [4],                            4]
]