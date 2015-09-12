__author__ = 'hanxuan'


"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


def unique_paths_with_obstacles(obstacle_grid):
    """
    :param obstacle_grid:
    :return:
    """
    if len(obstacle_grid) == 0 or len(obstacle_grid[0]) == 0:
        return 0

    if obstacle_grid[0][0] == 1:
        return 0

    return r(obstacle_grid, 0, 0, {})


def r(grid, i, j, d):
    """
    :param grid:
    :param i:
    :param j:
    :param d:
    :return:
    """

    if (i, j) in d:
        return d[(i, j)]

    if i == len(grid) - 1:
        obstacle_in_rode = False
        for k in range(j, len(grid[0])):
            if grid[i][k] == 1:
                obstacle_in_rode = True
                break
        re = 0 if obstacle_in_rode else 1
        d[(i, j)] = re
        return re

    if j == len(grid[0]) - 1:
        obstacle_in_rode = False
        for k in range(i, len(grid)):
            if grid[k][j] == 1:
                obstacle_in_rode = True
                break
        re = 0 if obstacle_in_rode else 1
        d[(i, j)] = re
        return re

    re = 0
    if grid[i + 1][j] != 1:
        re += r(grid, i + 1, j, d)
    if grid[i][j + 1] != 1:
        re += r(grid, i, j + 1, d)

    d[(i, j)] = re
    return re


if __name__ == '__main__':
    g0 = [
        [1]
    ]

    g1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    g2 = [
        [1, 0],
        [0, 0]
    ]

    print(unique_paths_with_obstacles(g0))
    print(unique_paths_with_obstacles(g1))
