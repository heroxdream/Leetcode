__author__ = 'hanxuan'


"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def generate_matrix(n):
    """
    :param n:
    :return:
    """
    if n == 0:
        return []

    n = abs(n)
    matrix = [[None] * n for _ in range(n)]
    recursive_generate(matrix, 1, (0, n - 1), (0, n - 1), (0, 0))
    return matrix


def recursive_generate(matrix, n, v_wall, h_wall, position):
    """
    :param n:
    :param v_wall:
    :param h_wall:
    :param position:
    :return:
    """
    if v_wall[0] > v_wall[1] or h_wall[0] > h_wall[1]:
        return

    i, j = position[0], position[1]
    if i == v_wall[0] and j == h_wall[0]:
        for k1 in range(h_wall[0], h_wall[1] + 1):
            matrix[i][k1] = n
            n += 1
        recursive_generate(matrix, n, (v_wall[0] + 1, v_wall[1]), h_wall, (i + 1, h_wall[1]))

    elif i == v_wall[0] and j == h_wall[1]:
        for k2 in range(v_wall[0], v_wall[1] + 1):
            matrix[k2][j] = n
            n += 1
        recursive_generate(matrix, n, v_wall, (h_wall[0], h_wall[1] - 1), (v_wall[1], j - 1))

    elif i == v_wall[1] and j == h_wall[1]:
        for k3 in range(h_wall[1], h_wall[0] - 1, -1):
            matrix[i][k3] = n
            n += 1
        recursive_generate(matrix, n, (v_wall[0], v_wall[1] - 1), h_wall, (i - 1, h_wall[0]))

    elif i == v_wall[1] and j == h_wall[0]:
        for k4 in range(v_wall[1], v_wall[0] - 1, -1):
            matrix[k4][j] = n
            n += 1
        recursive_generate(matrix, n, v_wall, (h_wall[0] + 1, h_wall[1]), (v_wall[0], j + 1))


if __name__ == '__main__':
    print(generate_matrix(1))
    print(generate_matrix(2))
    print(generate_matrix(3))
    print(generate_matrix(4))
