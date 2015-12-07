"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""


def calculate(s):
    ans = 0
    i = 0
    signs = [1, 1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            ans += signs.pop() * int(s[start:i])
            continue

        if c in '(-+':
            signs.append(signs[-1] * (1, -1)[c == '-'])
        elif c == ')':
            signs.pop()
        i += 1

    return ans
