"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0

    s_matrix = [[0] * len(matrix[0]) for _ in matrix]
    for i in range(len(matrix)):
        s_matrix[i][0] = int(matrix[i][0])

    for i in range(len(matrix[0])):
        s_matrix[0][i] = int(matrix[0][i])

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == '0':
                s_matrix[i][j] = 0
            else:
                s_matrix[i][j] = min(s_matrix[i-1][j], s_matrix[i-1][j-1], s_matrix[i][j-1]) + 1

    ans = -1
    for i in range(len(s_matrix)):
        for j in range(len(s_matrix[i])):
            if ans < s_matrix[i][j]:
                ans = s_matrix[i][j]
    return ans * ans
