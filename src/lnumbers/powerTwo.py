__author__ = 'hanxuan'


"""
Given an integer, write a function to determine if it is a power of two.
"""

def isPowerOfTwo(n):
    """

    :param n:
    :return:
    O(lgn) time: bad
    """
    if n <= 0:
        return False

    while n:
        if n % 2 != 0 and n != 1:
            return False
        n >>= 1

    return True


def isPowerOfTwoV2(n):
    """
    :param n:
    :return:

    O(1) time: very good
    """

    return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    print(isPowerOfTwoV2(0))
    print(isPowerOfTwoV2(1))
    print(isPowerOfTwoV2(2))
    print(isPowerOfTwoV2(7))
    print(isPowerOfTwoV2(8))
