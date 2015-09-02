__author__ = 'hanxuan'

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""

import string

def convertToTitle(n):
    """
    :param n: int > 0
    :return: string
    """
    table = dict(enumerate(string.ascii_uppercase))
    chars = []
    while n > 0:
        digit = 26 if n % 26 == 0 else n % 26
        chars.append(table[digit - 1])
        n = n // 26 if digit != 26 else n // 26 - 1
    return ''.join(chars[::-1])


if __name__ == '__main__':
    print(convertToTitle(1))
    print(convertToTitle(2))
    print(convertToTitle(25))
    print(convertToTitle(26))
    print(convertToTitle(27))
    print(convertToTitle(24568))