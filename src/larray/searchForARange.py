__author__ = 'hanxuan'


"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


def search_range(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

    if len(nums) == 0:
        return [-1, -1]

    return list(search(nums, 0, len(nums) - 1, target))


def search(a, l, r, t):
    """
    :param a: List[int]
    :param l: int
    :param r: int
    :param t: int
    :return: (int, int)
    """
    if l - r == 0:
        return (-1, -1) if a[l] != t else (l, r)

    mid = (l + r) // 2 + 1

    if a[mid] > t:
        return search(a, l, mid - 1, t)
    elif a[mid] < t:
        return search(a, mid, r, t)
    else:
        l1, r1 = search(a, l, mid - 1, t)
        l2, r2 = search(a, mid, r, t)
        l = l1 if l1 != -1 else mid
        r = r2 if r2 != -1 else mid
        return l, r


if __name__ == '__main__':
    n0 = [1]
    n1 = [5, 7, 7, 8, 8, 10]
    n2 = [1] * 1000

    print(search_range(n0, 1))
    print(search_range(n0, 2))

    print(search_range(n1, 2))
    print(search_range(n1, 6))
    print(search_range(n1, 7))
    print(search_range(n1, 8))
    print(search_range(n1, 10))

    print(search_range(n2, 1))

