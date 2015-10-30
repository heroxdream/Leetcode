__author__ = 'hanxuan'

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    if not tokens:
        return None

    operator = set(['+', '*', '/', '-'])
    stack = []
    for s in tokens:
        if s not in operator:
            stack.append(s)
        else:
            s2 = stack.pop()
            s1 = stack.pop()
            stack.append(calc(s1, s2, s))
    return int(stack.pop())


def calc(s1, s2, op):
    if op == '+':
        return int(s1) + int(s2)
    elif op == '-':
        return int(s1) - int(s2)
    elif op == '*':
        return int(s1) * int(s2)
    elif op == '/':
        return int(int(s1) * 1.0 / int(s2))