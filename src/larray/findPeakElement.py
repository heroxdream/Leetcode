__author__ = 'hanxuan'


"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

def r(nums, s, e):

    if s == e:
        return s

    if s + 1 == e:
        return s if nums[s] > nums[e] else e

    mid = (s + e) // 2

    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        return mid
    elif nums[mid - 1] < nums[mid]:
        return r(nums, mid + 1, e)
    elif nums[mid - 1] > nums[mid]:
        return r(nums, s, mid - 1)

if __name__ == '__main__':

    n0 = [1, 2]
    n1 = [2, 1, 2]
    n2 = [1, 3, 2]
    n3 = [1, 2, 3, 4]

    print(r(n0, 0, len(n0) - 1))
    print(r(n1, 0, len(n1) - 1))
    print(r(n2, 0, len(n2) - 1))
    print(r(n3, 0, len(n3) - 1))
