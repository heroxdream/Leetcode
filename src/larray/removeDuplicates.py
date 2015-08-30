__author__ = 'hanxuan'


def removeDuplicates(nums):

    """
    :param nums: List[int]
    :return: int
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new
    length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    For example,
    Given input array nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    """

    p = 0
    n = len(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[p]:
            n -= 1
        else:
            nums[p + 1] = nums[i]
            p += 1

    print(nums)

    return n


if __name__ == '__main__':
    print(removeDuplicates([1, 2, 3, 3]))
    print(removeDuplicates([1]))
    print(removeDuplicates([1, 1, 2]))
    print(removeDuplicates([]))
