__author__ = 'hanxuan'
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of
money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police if two adjacent houses were
broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the
maximum amount of money you can rob tonight without alerting the police.
"""

def rob(nums):
    return 0 if len(nums) == 0 else rob_with_mem(nums, {})

def rob_with_mem(nums, record):
    if len(nums) in record:
        return record[len(nums)]

    if len(nums) == 1:
        record[len(nums)] = nums[0]
        return record[len(nums)]

    if len(nums) == 2:
        record[len(nums)] = max(nums[0], nums[1])
        return record[len(nums)]

    curr_max = max(nums[0] + rob_with_mem(nums[2:], record), rob_with_mem(nums[1:], record))
    record[len(nums)] = curr_max
    return curr_max

if __name__ == '__main__':
    print(rob([]))
    print(rob([1, 2, 3, 8]))
    print(rob([1, 9, 3, 11]))
