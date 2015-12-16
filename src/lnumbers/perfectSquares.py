"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    counter = 1
    ret = [9999999999] * (n + 1)
    ret[0] = 0
    while counter <= n:

        i = 0
        while i * i <= counter:
            ret[counter] = min(ret[counter], ret[counter - i * i] + 1)
            i += 1

            counter += 1

    return ret[-1]
