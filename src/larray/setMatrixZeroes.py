__author__ = 'hanxuan'


"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


# def set_zeros(matrix):
#     """
#     :param matrix:
#     :return:
#     """
#     if not matrix or len(matrix[0]) == 0:
#         return
#
#     ncol = len(matrix[0])
#
#     set_matrix_zeros(matrix, 0, (0, ncol - 1))
#
#
# def set_matrix_zeros(m, row_start, col_boundary):
#     """
#     :param m: List[List[int]]
#     :return: void
#     """
#
#     nrow = len(m)
#     if row_start >= nrow:
#         return
#
#     col_start, col_end = col_boundary[0], col_boundary[1]
#     if col_end < col_start:
#         return
#
#     zero_cols = [idx for idx in check_row(m, row_start, col_boundary)]
#     if zero_cols:
#         col_start_temp = col_start
#         for col in zero_cols:
#             set_zeros_col(m, col)
#             set_matrix_zeros(m, row_start + 1, (col_start_temp, col - 1))
#             col_start_temp = col + 1
#         set_matrix_zeros(m, row_start + 1, (zero_cols[-1] + 1, col_end))
#         set_zeros_row(m, row_start, col_boundary)
#     else:
#         set_matrix_zeros(m, row_start + 1, col_boundary)
#
#
# def check_row(m, row, col_boundary):
#     """
#     :param m:
#     :param row:
#     :param col_boundary:
#     :return:
#     """
#     for i in range(col_boundary[0], col_boundary[1] + 1):
#         if m[row][i] == 0:
#             yield i
#
#
# def set_zeros_row(m, row, col_boundary):
#     """
#     :param m:
#     :param row:
#     :param col_boundary:
#     :return:
#     """
#     for i in range(col_boundary[0], col_boundary[1] + 1):
#         m[row][i] = 0
#
#
# def set_zeros_col(m, col):
#     """
#     :param m:
#     :param col:
#     :return:
#     """
#     for i in range(len(m)):
#         m[i][col] = 0


def set_zeros(matrix):
    """
    :param matrix:
    :return:
    """
    col0 = 1
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col0 = 0
            break

    for i in range(len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    print('m:', matrix)

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0

    if col0 == 0:
        for i in range(len(matrix)):
            matrix[i][0] = 0


if __name__ == '__main__':

    from pprint import pprint as show

    m0 = [
        [0]
    ]

    m1 = [
        [1, 2, 3],
        [1, 2, 0],
        [0, 1, 2]
    ]

    m11 = [
        [0, 2, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]

    m2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    m3 = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ]

    m4 = [
        [0, 0, 0, 5],
        [4, 3, 1, 4],
        [0, 1, 1, 4],
        [1, 2, 1, 3],
        [0, 0, 1, 1]
    ]

    m5 = [
        [1, 1, 1],
        [0, 1, 2]
    ]

    set_zeros(m0)
    show(m0)

    set_zeros(m1)
    show(m1)

    set_zeros(m2)
    show(m2)

    set_zeros(m3)
    show(m3)

    set_zeros(m4)
    show(m4)

    set_zeros(m5)
    show(m5)
