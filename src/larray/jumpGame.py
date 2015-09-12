__author__ = 'hanxuan'


"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return recursive_can_jump(nums, 0, {})


def recursive_can_jump(nums, start, record):
    """
    :param nums:
    :param start:
    :return:
    """

    if start in record:
        return record[start]

    if start >= len(nums) - 1:
        return True

    if nums[start] == 0:
        return False

    max_step = nums[start]
    for step in range(1, max_step + 1):
        if recursive_can_jump(nums, start + step, record):
            record[start] = True
            return True
    record[start] = False
    return False


def can_jump_v2(nums):

    zeros = []
    pointer = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append((pointer, i))
            pointer = i + 1

    for start, end in zeros:
        pointer = end
        while True:
            if pointer == -1:
                return False
            if nums[pointer] > end - pointer:
                break
            if nums[pointer] == end - pointer and end == len(nums) - 1:
                break

            pointer -= 1

    return True

def can_jump_v3(nums):
    tail = len(nums)
    p = 0
    max_reach = 0
    while p < len(nums) and p <= max_reach:
        max_reach = max(p + nums[p], max_reach)
        p += 1
    return p == tail


if __name__ == '__main__':
    n0 = [2, 3, 1, 1, 4]
    n1 = [3, 2, 1, 0, 4]
    n2 = [0, 0, 0, 0]
    n3 = [0]
    n4 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    n5 = [2, 0, 0]

    # print(can_jump(n0))
    # print(can_jump(n1))
    # print(can_jump(n2))
    # print(can_jump(n3))
    # print(can_jump(n4))

    # print(can_jump_v2(n0))
    # print(can_jump_v2(n1))
    # print(can_jump_v2(n2))
    # print(can_jump_v2(n3))
    # print(can_jump_v2(n4))
    # print(can_jump_v2(n5))

    print(can_jump_v3(n0))
    print(can_jump_v3(n1))
    print(can_jump_v3(n2))
    print(can_jump_v3(n3))
    print(can_jump_v3(n4))
    print(can_jump_v3(n5))
