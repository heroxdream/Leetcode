__author__ = 'hanxuan'



"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def singleNumber(nums):
    """
    :param nums:
    :return:
    """
    filter = set()
    for i in range(len(nums)):
        if nums[i] in filter:
            filter.remove(nums[i])
        else:
            filter.add(nums[i])
    return filter.pop()

def singleNumber2(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


if __name__ == '__main__':
    print(singleNumber2([1, 1, 3]))
