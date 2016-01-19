__author__ = 'hanxuan'


def twoSum(nums, target):

    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

    table = {}
    for i in range(len(nums)):
        if target - nums[i] in table:
            res = [table[target - nums[i]], i]
            return res
        table[nums[i]] = i
    return [0] * 2

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
