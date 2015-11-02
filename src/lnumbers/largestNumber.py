__author__ = 'hanxuan'


"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    Input:     [0,0]
    Output:    "00"
    Expected:  "0"
    """
    nums = [str(s) for s in nums]
    nums.sort(key=lambda x, y: (x > y) - (x < y))
    return ''.join(nums).lstrip('0') or '0'


def cmp2(a, b):
    return (a > b) - (a < b)

if __name__ == '__main__':
    print(largestNumber([1, 2, 4]))
