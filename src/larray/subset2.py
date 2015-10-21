__author__ = 'hanxuan'


"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


def subsetsWithDup(nums):

    """
    :param nums:
    :return:
    """
    seen = set()
    return subsets_recursive(nums, seen)


def subsets_recursive(nums, seen):

    if len(nums) == 0:
        return [[]]

    num_current = nums[0]
    num_rest = nums[1:]

    rest_result = subsets_recursive(num_rest, seen)
    re = []
    for l in rest_result:
        new_l = l[:]
        new_l.append(num_current)
        new_l.sort()
        id_l = identity(new_l)
        if id_l in seen:
            continue
        else:
            seen.add(id_l)
        re.append(new_l)

    return rest_result + re


def identity(array):
    """
    :param array:
    :return:
    """

    re = []
    for x in array:
        re.append(str(x))
    return ''.join(re)


if __name__ == '__main__':
    n0 = [1, 2, 2]
    print(subsetsWithDup(n0))
