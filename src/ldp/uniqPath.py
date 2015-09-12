__author__ = 'hanxuan'


"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

def unique_paths(m, n):
    """
    :param m:
    :param n:
    :return:
    """
    if m == 0 or n == 0:
        return 0

    return unique_path_record(m, n, {})


def unique_path_record(m, n, d):
    """
    :param m:
    :param n:
    :param d:
    :return:
    """

    if (m, n) in d:
        return d[(m, n)]

    if m == 1 or n == 1:
        return 1

    re = unique_path_record(m - 1, n, d) + unique_path_record(m, n - 1, d)

    d[(m, n)] = re
    return re



if __name__ == '__main__':
    print(unique_paths(1, 1))
    print(unique_paths(2, 2))
    print(unique_paths(2, 3))

