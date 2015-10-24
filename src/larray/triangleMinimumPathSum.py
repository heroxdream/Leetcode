__author__ = 'hanxuan'



"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


def minimumTotal(triangle):

    if not triangle or not triangle[0]:
        return 0

    return recursive_with_dict(triangle, {}, 0, 0)

def recursive_with_dict(triangle, d, i, j):
    """
    O(n^2) space
    """

    if (i, j) in d:
        return d[(i, j)]

    if i == len(triangle) - 1:
        d[(i, j)] = triangle[i][j]
        return d[(i, j)]

    min_sum = min(recursive_with_dict(triangle, d, i + 1, j),
                  recursive_with_dict(triangle, d, i + 1, j + 1)) + triangle[i][j]
    d[(i, j)] = min_sum

    return d[(i, j)]

def recursive_with_dict_v2(triangle, d, i, j):
    """
    O(n) space
    """

    if (i, j) in d:
        ans = d[(i, j)]
        d.pop((i, j))
        return ans

    if i == len(triangle) - 1:
        d[(i, j)] = triangle[i][j]
        return d[(i, j)]

    min_sum = min(recursive_with_dict(triangle, d, i + 1, j),
                  recursive_with_dict(triangle, d, i + 1, j + 1)) + triangle[i][j]
    d[(i, j)] = min_sum

    return d[(i, j)]