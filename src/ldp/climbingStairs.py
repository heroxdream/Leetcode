__author__ = 'hanxuan'
"""
    :param n: int
    :return: int
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbingStairsV1(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbingStairsV1(n - 1) + climbingStairsV1(n - 2)

def climbingStairsV2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    x1 = 1
    x2 = 2
    ways = 0
    for _ in range(0, n - 2):
        ways += x1 + x2
        x1 = x2
        x2 = ways

    return ways
