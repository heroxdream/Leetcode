__author__ = 'hanxuan'
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those
numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

def isHappy(n):
    """
    :param n: int
    :return: bool
    """

    circle = set()
    while True:
        nn = sum(map(lambda x: int(x) ** 2, str(n)))
        if nn in circle:
            break
        circle.add(nn)
        n = nn
    return True if 1 in circle else False


def isHappyV2(n):
    """
    :param n: int
    :return: bool

    Floyd circle detection algorithm:
    https://en.wikipedia.org/wiki/Cycle_detection
    """
    slow = n
    fast = sum(map(lambda x: int(x) ** 2, str(n)))
    while slow != fast:
        slow = sum(map(lambda x: int(x) ** 2, str(slow)))
        fast = sum(map(lambda x: int(x) ** 2, str(fast)))
        fast = sum(map(lambda x: int(x) ** 2, str(fast)))

    return slow == 1

if __name__ == '__main__':
    print(isHappy(21))
    print(isHappyV2(21))
