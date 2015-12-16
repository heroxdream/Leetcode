def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    p1 = 0
    while p1 < len(nums) and nums[p1] != 0:
        p1 += 1

    p2 = p1
    while p2 < len(nums) and nums[p2] == 0:
        p2 += 1

    while p2 < len(nums):
        while p1 < len(nums) and nums[p1] != 0: p1 += 1
        while p2 < len(nums) and nums[p2] == 0: p2 += 1
        if p2 == len(nums): break

        swap(nums, p1, p2)


def swap(nums, p1, p2):
    tmp = nums[p1]
    nums[p1] = nums[p2]
    nums[p2] = tmp
