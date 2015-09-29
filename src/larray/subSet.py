__author__ = 'hanxuan'

"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def sub_sets(nums):
    """
    :param nums:
    :return:
    """

    if len(nums) == 0:
        return [[]]

    curr = nums[0]
    rest = nums[1:]

    sub = sub_sets(rest)
    copy = [i[:] for i in sub]
    for e in copy:
        e.append(curr)
        e.sort()
    return copy + sub


if __name__ == '__main__':
    n0 = [1, 2, 3]
    print(sub_sets(n0))
