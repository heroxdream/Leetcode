__author__ = 'hanxuan'


"""
"""


def quickSort(nums):
    """
    :param nums:
    :return:
    """

    sort(nums, 0, len(nums))


def sort(nums, start, end):
    """
    :param nums:
    :param start:
    :param end:
    :return:
    """

    if start + 1 >= end:
        return

    partition_index = partition(nums, start, end)
    sort(nums, start, partition_index)
    sort(nums, partition_index + 1, end)


def partition(nums, start, end):

    i = start
    j = end - 1

    pivot = nums[(i + j) // 2]

    while i <= j:

        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i += 1
            j -= 1

    return i


if __name__ == '__main__':
    n0 = [3, 2, 1]
    quickSort(n0)
    print(n0)

    n0 = [3, 2, 1, 1, 2, 3]
    quickSort(n0)
    print(n0)

    n0 = [1] * 100
    quickSort(n0)
    print(n0)
