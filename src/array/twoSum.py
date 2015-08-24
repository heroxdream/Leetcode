__author__ = 'hanxuan'


def twoSum(nums, target):

    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

    print(nums)
    print(target)

    nums_dict = {}
    for i, num in enumerate(nums, 1):
        nums_dict[num] = i

    for i, num in enumerate(nums, 1):
        remain  = target - num
        if remain in nums_dict and nums_dict[remain] != i:
            return [i, nums_dict[remain]]



if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
