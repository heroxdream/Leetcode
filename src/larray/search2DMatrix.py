__author__ = 'hanxuan'



"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


def search_matrix(matrix, target):
    """
    :param matrix:
    :param target:
    :return:
    """

    if not matrix or len(matrix[0]) == 0:
        return False

    return r(matrix, 0, len(matrix), target)


def r(matrix, rs, re, t):
    """
    :param matrix:
    :param rs:
    :param re:
    :param t:
    :return:
    """

    if rs == re:
        return False

    if rs + 1 == re:
        return binary_search(matrix, rs, 0, len(matrix[0]), t)

    mid_r = (rs + re) // 2
    mid_r_v1 = matrix[mid_r][0]
    mid_r_v2 = matrix[mid_r][len(matrix[0]) - 1]
    if mid_r_v1 <= t <= mid_r_v2:
        return r(matrix, mid_r, mid_r + 1, t)
    elif t < mid_r_v1:
        return r(matrix, rs, mid_r, t)
    elif t > mid_r_v2:
        return r(matrix, mid_r + 1, re, t)


def binary_search(matrix, row, cs, ce, target):
    """
    :param matrix:
    :param row:
    :param cs:
    :param ce:
    :param target:
    :return:
    """

    if cs == ce:
        return False

    if cs + 1 == ce:
        return True if matrix[row][cs] == target else False

    mid = (cs + ce) // 2
    if matrix[row][mid] == target:
        return True
    elif matrix[row][mid] > target:
        return binary_search(matrix, row, cs, mid, target)
    else:
        return binary_search(matrix, row, mid + 1, ce, target)


if __name__ == '__main__':
    m0 = [
        [1]
    ]

    m1 = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    m2 = [
        [1, 1]
    ]

    m3 = [
        [1, 1],
        [2, 2]
    ]

    print(search_matrix(m0, 1))
    print(search_matrix(m0, 0))
    print(search_matrix(m1, 1))
    print(search_matrix(m1, 100))
    print(search_matrix(m1, 0))
    print(search_matrix(m1, 10))
    print(search_matrix(m2, 1))
    print(search_matrix(m2, 2))
    print(search_matrix(m3, 3))
