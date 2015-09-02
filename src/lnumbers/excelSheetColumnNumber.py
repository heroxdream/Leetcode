__author__ = 'hanxuan'

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""

def titleToNumber(s):
    """
    :param s: string
    :return: int
    """
    uppercase = 'abcdefghijklmnopqrstuvwxyz'.upper()
    table = dict(map(lambda x: (x[1], x[0] + 1), enumerate(uppercase)))

    pointer = len(s) - 1
    x = 0
    weight = 1
    while pointer >= 0:
        x += table[s[pointer]] * weight
        pointer -= 1
        weight *= 26
    return x


if __name__ == '__main__':
    print(titleToNumber('A'))
    print(titleToNumber('Z'))
    print(titleToNumber('AA'))
    print(titleToNumber('AB'))