__author__ = 'hanxuan'

def removeElements(nums, val):
    """
    :param nums: List[int]
    :param val: int
    :return: int

    """

    p = 0
    n = len(nums)
    for i in range(0, len(nums)):
        if nums[i] == val:
            n -= 1
        else:
            nums[p] = nums[i]
            p += 1
    print(nums)
    return n


if __name__ == '__main__':
    print(removeElements([1, 1, 2, 3], 1))
    print(removeElements([1, 1, 2, 3], 2))
    print(removeElements([1, 1, 2, 3], 3))
    print(removeElements([1, 1, 2, 3], 5))