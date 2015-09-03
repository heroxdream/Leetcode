__author__ = 'hanxuan'

"""
(1) Given an array of integers, find if the array contains any duplicates. Your function should return
true if any value appears at least twice in the array, and it should return false if every element is distinct.


(2) Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""


def containsDuplicate(nums):
    """
    :param nums: List[int]
    :return: bool
    """

    seen = set(nums)
    return len(seen) != len(nums)


def containsNearbyDuplicate(nums, k):
    """
    :param nums:
    :param k:
    :return:
    """

    groups = dict()
    for i in range(len(nums)):
        if nums[i] not in groups:
            groups[nums[i]] = [i]
        else:
            groups[nums[i]].append(i)

    for key in filter(lambda x: len(groups[x]) > 1, groups.keys()):
        indexes = sorted(groups[key])
        indexes.append(indexes[0])
        gaps = []
        for i in range(len(indexes) - 1):
            gaps.append(abs(indexes[i + 1] - indexes[i]))
        if min(gaps) <= k:
            return True

    return False


def containsNearbyDuplicateV3(nums, k):
    """
    :param nums:
    :param k:
    :return:

    sliding window
    """
    window = set()
    for i in range(k + 1):
        if nums[i] in window:
            return True
        window.add(nums[i])

    for i in range(k + 1, len(nums)):
        window.remove(nums[i - k - 1])
        if nums[i] in window:
            return True
        window.add(nums[i])

    return False


if __name__ == '__main__':
    print(containsNearbyDuplicate([1, 2, 3, 2, 1], 1))
    print(containsNearbyDuplicateV3([1, 2, 3, 2, 1], 1))
