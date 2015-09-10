__author__ = 'hanxuan'


"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""


def permute(nums):
    """
    :param nums: List[int]
    :return: List[List[int]]
    """

    nums.sort()

    re = [nums[:]]
    for _ in range(factorial(len(nums)) - 1):
        p = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                p = i
        pp = len(nums) - 1
        while True:
            if nums[pp] > nums[p - 1]:
                break
            pp -= 1

        t = nums[p - 1]
        nums[p - 1] = nums[pp]
        nums[pp] = t

        reverse(nums, p, len(nums) - 1)

        re.append(nums[:])

    return re


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def reverse(a, p1, p2):
    """
    :param a: List[int]
    :param p1: int
    :param p2: int
    :return: void
    """
    while p1 < p2:
        t = a[p1]
        a[p1] = a[p2]
        a[p2] = t
        p1 += 1
        p2 -= 1



if __name__ == '__main__':
    n0 = [3, 1, 2]
    print(permute(n0))
