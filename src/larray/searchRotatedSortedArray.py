__author__ = 'hanxuan'

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

def search(nums, target):
    """
    :param nums:
    :param target:
    :return:
    """
    return -1 if not nums else recursive_search(nums, 0, len(nums), target)

def recursive_search(nums, start, end, target):
    """
    :param nums:
    :param start:
    :param end:
    :param target:
    :return:
    """

    if start >= end:
        return -1

    if start + 1 == end:
        return -1 if nums[start] != target else start

    mid = (start + end) // 2
    if nums[mid] == target:
        return mid

    if nums[start] >= nums[end - 1]:
        left = recursive_search(nums, start, mid, target)
        if left != -1:
            return left
        return recursive_search(nums, mid + 1, end, target)
    else:
        if target > nums[mid]:
            return recursive_search(nums, mid + 1, end, target)
        else:
            return recursive_search(nums, start, mid, target)


def search_v2(nums, target):
    """
    :param nums:
    :param target:
    :return:
    """

    if not nums:
        return False
    index = recursive_search(nums, 0, len(nums), target)

    return True if index != -1 else False


if __name__ == '__main__':
    n0 = [4, 5, 5, 5, 6, 7, 7, 7, 0, 1, 2, 2]
    for n in n0:
        print('{} {}'.format(n, search_v2(n0, n)))

    print(search(n0, 3))
