__author__ = 'hanxuan'


"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


def search_insert(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: int
    """

    if len(nums) == 0:
        return 0

    return search(nums, 0, len(nums) - 1, target)


def search(a, l, r, t):
    """
    :param a: List[int]
    :param l: int
    :param r: int
    :param t: int
    :return: int
    """

    if l == r:
        if a[l] == t:
            return l
        else:
            return max(0, l - 1) if t < a[l] else l + 1

    mid = (l + r) // 2 + 1

    if a[mid] > t:
        return search(a, l, mid - 1, t)
    elif a[mid] < t:
        return search(a, mid, r, t)
    else:
        return mid


if __name__ == '__main__':
    n0 = [1, 3, 5, 6]
    print(search_insert(n0, 5))
    print(search_insert(n0, 2))
    print(search_insert(n0, 7))
    print(search_insert(n0, 4))
    print(search_insert(n0, 0))
