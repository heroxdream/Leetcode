__author__ = 'hanxuan'


"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def singleNumber(nums):
    """
    :param nums:
    :return:
    """

    count = [0] * 32
    result = 0
    for i in range(32):
        for j in range(len(nums)):
            if (nums[j] >> i) & 1:
                count[i] += 1

        result |= ((count[i] % 3) << i)

    print(count)
    print(result)
    return result


if __name__ == '__main__':
    singleNumber([1, 1, 1, 3, 3])
    singleNumber([-1, -1, -1, 3, 3])
    singleNumber([1, 1, 1, 3, 3, 2, 2, 2])
    singleNumber([1, 1, 1, 3, 2, 2, 2])
    singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])


