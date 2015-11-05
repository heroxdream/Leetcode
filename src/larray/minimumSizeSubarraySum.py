__author__ = 'hanxuan'


"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    end = start = 0
    min_len = len(nums) + 1
    window_sum = 0
    while start < len(nums):
        window_sum += nums[start]
        start += 1

        while window_sum >= s:
            min_len = min(min_len, start - end)
            window_sum -= nums[end]
            end += 1
    return 0 if min_len == len(nums) + 1 else min_len


