__author__ = 'hanxuan'


"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""


def permute_unique(nums):
    """
    :param nums: List[int]
    :return: List[List[int]]
    """

    if len(nums) == 0:
        return []

    nums.sort()
    re = [nums[:]]
    while True:
        p = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                p = i
        if p == -1:
            break

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


def reverse(a, p1, p2):
    while p1 < p2:
        t = a[p1]
        a[p1] = a[p2]
        a[p2] = t
        p1 += 1
        p2 -= 1


if __name__ == '__main__':
    n0 = [1, 2, 1]
    n1 = [1, 1, 1]
    n2 = [1, 1, 1, 3]
    n3 = [1, 2, 3]
    print(permute_unique(n0))
    print(permute_unique(n1))
    print(permute_unique(n2))
    print(permute_unique(n3))
