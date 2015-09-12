__author__ = 'hanxuan'


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in tim
"""


def mini_path_sum(grid):
    """
    :param grid:
    :return:
    """

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    return r(grid, 0, 0, {})


def r(grid, i, j, d):
    """
    :param grid:
    :param i:
    :param j:
    :param d:
    :return:
    """
    if (i, j) in d:
        return d[i, j]

    if i == len(grid) - 1:
        d[(i, j)] = 0
        for k in range(j, len(grid[0])):
            d[(i, j)] += grid[i][k]
        return d[(i, j)]

    if j == len(grid[0]) - 1:
        d[(i, j)] = 0
        for k in range(i, len(grid)):
            d[(i, j)] += grid[k][j]
        return d[(i, j)]

    d[(i, j)] = min(r(grid, i + 1, j, d), r(grid, i, j + 1, d)) + grid[i][j]
    return d[(i, j)]

if __name__ == '__main__':
    g0 = [
        [1, 0, 0],
        [4, 5, 0],
        [7, 8, 0]
    ]

    print(mini_path_sum(g0))
