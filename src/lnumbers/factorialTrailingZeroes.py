__author__ = 'hanxuan'

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

def trailingZeroes(n):
    """
    :param n: int
    :return: int
    """

    p = 0
    while True:
        if pow(5, p + 1) > n:
            break
        p += 1

    x = 0
    while p > 0:
        x += n // pow(5, p)
        p -= 1

    return x


if __name__ == '__main__':
    print(trailingZeroes(0))
    print(trailingZeroes(1))
    print(trailingZeroes(5))
    print(trailingZeroes(10))
    print(trailingZeroes(25))
    print(trailingZeroes(30))
    print(trailingZeroes(50))