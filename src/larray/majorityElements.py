__author__ = 'hanxuan'
"""
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.

how about O(n) time and O(1) space
"""

def majorityElementV1(nums):
    counter = {}
    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[0][0]

def majorityElementV2(nums):
    nums = sorted(nums, reverse=True)
    return nums[len(nums) // 2]

def majorityElementV3(nums):
    """
    :param nums: List[int]
    :return: int
    This can be solved by Moore's voting algorithm. Basic idea of the algorithm is
    if we cancel out each occurrence of an element e with all the other elements that
    are different from e then e will exist till end if it is a majority element.
    """
    counter = 0
    majority = nums[0]
    for i in range(len(nums)):
        if counter == 0:
            majority = nums[i]
            counter = 1
            continue
        if nums[i] == majority:
            counter += 1
        else:
            counter -= 1
    return majority


if __name__ == '__main__':
    print(majorityElementV1([1, 2, 3, 4, 1, 2, 1]))
    print(majorityElementV2([1, 2, 3, 4, 1, 1, 1]))
    print(majorityElementV3([1, 2, 3, 4, 1, 1, 1]))
