__author__ = 'hanxuan'

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional
elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


def merge(nums1, m, nums2, n):
    """
    :param nums1: List[int]
    :param m: int
    :param nums2: List[int]
    :param n: int
    :return: void Do not return anything, modify nums1 in-place instead.
    """

    # pointer = len(nums1) - 1
    pointer = m + n - 1
    pointer1 = m - 1
    pointer2 = n - 1
    while pointer1 >= 0 and pointer2 >= 0:
        if nums1[pointer1] >= nums2[pointer2]:
            nums1[pointer] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[pointer] = nums2[pointer2]
            pointer2 -= 1
        pointer -= 1

    while pointer1 >= 0:
        nums1[pointer] = nums1[pointer1]
        pointer -= 1
        pointer1 -= 1

    while pointer2 >= 0:
        nums1[pointer] = nums2[pointer2]
        pointer -= 1
        pointer2 -= 1

    # head = 0
    # pointer += 1
    # for _ in range(m + n):
    #     nums1[head] = nums1[pointer]
    #     head += 1
    #     pointer += 1

if __name__ == '__main__':
    nums1 = [1, 2, 3, -1, -1, -1, -1, -1]
    nums2 = [4, 5, 6, 7]
    merge(nums1, 3, nums2, 4)
    print(nums1)