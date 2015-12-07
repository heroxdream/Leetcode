"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
Do you have a better hint? Suggest it!

"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums: return []

    count1, count2, candidate1, candidate2 = 0, 0, 0, 0
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            count1, candidate1 = 1, n
        elif count2 == 0:
            count2, candidate2 = 1, n
        else:
            count1 -= 1
            count2 -= 1

    ans = []
    for n in set([candidate1, candidate2]):
        if nums.count(n) > len(nums) // 3:
            ans.append(n)

    return ans


    # return [n for n in set([candidate1, candidate2]) if nums.count(n) > len(nums) // 3]