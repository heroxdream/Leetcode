"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


def lengthOfLIS(nums):

    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    n = len(nums)
    lis = [1] * n

    for i in range(0, n):
        for j in range(0, i):
            if nums[j] < nums[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0
    for i in range(0, n):
        maximum = max(maximum, lis[i])

    return maximum
