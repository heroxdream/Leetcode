__author__ = 'hanxuan'

def findMedianSortedArrays(nums1, nums2):
    """
    find the median of two sorted arrays.

    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    l1 = len(nums1)
    l2 = len(nums2)

    if (l1 + l2) % 2 == 0:
        return (findKth(nums1, 0, nums2, 0, int((l1 + l2) / 2)) +
                findKth(nums1, 0, nums2, 0, int((l1 + l2) / 2 + 1))) * 1.0 / 2
    else:
        return findKth(nums1, 0, nums2, 0, int((l1 + l2) / 2) + 1)


def findKth(long_array, long_pointer, short_array, short_pointer, k):
    """
    find the Kth max or min element in two sorted arrays.

    :param long_array: List[int]
    :param long_pointer: int
    :param short_array: List[int]
    :param short_pointer: int
    :param k: int
    :return: int
    """

    # we always assume that long_array always has longer logical length.
    if len(long_array) - long_pointer < len(short_array) - short_pointer:
        return findKth(short_array, short_pointer, long_array, long_pointer, k)

    # if the short_array is logically empty, return the logically Kth element in long_array
    if len(short_array) - short_pointer == 0:
        return long_array[long_pointer + k - 1]

    # get to the point that find the 1st minimum element
    if k == 1:
        return min(long_array[long_pointer], short_array[short_pointer])

    # be careful about the short, long array skip len, their sum should be k
    short_array_skip_len = min(int(k / 2), len(short_array) - short_pointer)
    long_array_skip_len = k - short_array_skip_len

    if long_array[long_pointer + long_array_skip_len - 1] == short_array[short_pointer + short_array_skip_len - 1]:
        return long_array[long_pointer + long_array_skip_len - 1]
    elif long_array[long_pointer + long_array_skip_len - 1] > short_array[short_pointer + short_array_skip_len - 1]:
        return findKth(long_array, long_pointer, short_array, short_pointer + short_array_skip_len, k - short_array_skip_len)
    else:
        return findKth(long_array, long_pointer + long_array_skip_len, short_array, short_pointer, k - long_array_skip_len)

if __name__ == '__main__':
    a1 = [1, 2]
    a2 = [1, 2]
    print(findKth(a1, 0, a2, 0, 2))
    print(findKth(a1, 0, a2, 0, 3))
    # print(findKth(a1, 0, a2, 0, 3))
    # print(findKth(a1, 0, a2, 0, 4))
    # print(findKth(a1, 0, a2, 0, 5))
    # print(findKth(a1, 0, a2, 0, 6))
    # print(findKth(a1, 0, a2, 0, 7))

    print(findMedianSortedArrays(a1, a2))
