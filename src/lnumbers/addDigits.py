__author__ = 'hanxuan'


"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


def addDigits(num):

    if num == 0:
        return 0
    else:
        return 9 if num % 9 == 0 else num % 9

if __name__ == '__main__':
    print(addDigits(38))
    print(addDigits(99))
    print(addDigits(1024))
