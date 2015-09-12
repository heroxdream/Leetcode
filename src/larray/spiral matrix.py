__author__ = 'hanxuan'


"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


def spiral_order(matrix):
    """
    :param matrix: List[List[int]]
    :return: List[int]
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []

    result = []
    m = len(matrix)
    n = len(matrix[0])
    spiral(matrix, (0, n - 1), (0, m - 1), (0, 0), result)
    return result


def spiral(matrix, h_wall, v_wall, pointer, accumulator):
    """
    :param matrix:
    :param h_wall:
    :param v_wall:
    :param pointer:
    :param accumulator:
    :return:
    """

    print(h_wall, v_wall, pointer, accumulator)

    if v_wall[0] > v_wall[1] or h_wall[0] > h_wall[1]:
        return

    i, j = pointer[0], pointer[1]
    if i == v_wall[0] and j == h_wall[0]:
        print('in 1')
        for k1 in range(h_wall[0], h_wall[1] + 1):
            accumulator.append(matrix[i][k1])
        spiral(matrix, h_wall, (v_wall[0] + 1, v_wall[1]), (i + 1, h_wall[1]), accumulator)

    elif i == v_wall[0] and j == h_wall[1]:
        print('in 2')
        for k2 in range(v_wall[0], v_wall[1] + 1):
            accumulator.append(matrix[k2][j])
        spiral(matrix, (h_wall[0], h_wall[1] - 1), v_wall, (v_wall[1], j - 1), accumulator)

    elif i == v_wall[1] and j == h_wall[1]:
        print('in 3')
        for k3 in range(h_wall[1], h_wall[0] - 1, -1):
            accumulator.append(matrix[i][k3])
        spiral(matrix, h_wall, (v_wall[0], v_wall[1] - 1), (i - 1, h_wall[0]), accumulator)

    elif i == v_wall[1] and j == h_wall[0]:
        print('in 4')
        for k4 in range(v_wall[1], v_wall[0] - 1, -1):
            accumulator.append(matrix[k4][j])
        spiral(matrix, (h_wall[0] + 1, h_wall[1]), v_wall, (v_wall[0], j + 1), accumulator)


if __name__ == '__main__':
    m0 = [
        [1]
    ]
    m1 = [
        [1, 2],
        [3, 4]
    ]
    m2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    m3 = [
        [1, 2]
    ]

    print(spiral_order(m0))
    print(spiral_order(m1))
    print(spiral_order(m2))
    print(spiral_order(m3))
