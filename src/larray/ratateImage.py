__author__ = 'hanxuan'


"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


def rotate_matrix(matrix):
    """
    :param matrix: List[List[int]]
    :return: void In-place modify
    x1 x2 x3
    x4 x5 x6
    x7 x8 x9
    =>
    x7 x4 x1
    x8 x5 x2
    x9 x6 x3
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return

    horizontal_reverse(matrix)
    diagonal_reverse(matrix)


def horizontal_reverse(matrix):
    """
    :param matrix: List[List[int]]
    :return: void In-place modify

    x1 x2
    x3 x4
    =>
    x2 x1
    x4 x3
    """

    for i in range(len(matrix)):
        vector = matrix[i]
        p1, p2 = 0, len(vector) - 1
        while p1 < p2:
            t = vector[p1]
            vector[p1] = vector[p2]
            vector[p2] = t
            p1 += 1
            p2 -= 1


def diagonal_reverse(matrix):
    """
    :param matrix: square matrix
    :return:
    """

    n = len(matrix)
    for i in range(n):
        for j in range(n - i):
            t = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][n - 1 - i]
            matrix[n - 1 - j][n - 1 - i] = t


if __name__ == '__main__':
    m0 = [[1, 2], [3, 4]]
    # horizontal_reverse(m0)
    # print(m0)
    # diagonal_reverse(m0)
    # rotate_matrix(m0)
    # print(m0)

    m1 = [[]]
    rotate_matrix(m1)
    print(m1)
