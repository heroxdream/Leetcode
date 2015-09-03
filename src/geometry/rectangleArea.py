__author__ = 'hanxuan'

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""


def computeArea(A, B, C, D, E, F, G, H):
    """
    :param A: int
    :param B: int
    :param C: int
    :param D: int
    :param E: int
    :param F: int
    :param G: int
    :param H: int
    :return: int
    """

    a1 = rectangle_area((A, B), (C, D))
    a2 = rectangle_area((E, F), (G, H))

    x_over_lap = line_over_lap_len((A, C), (E, G))
    y_over_lap = line_over_lap_len((B, D), (F, H))
    return a1 + a2 - (x_over_lap * y_over_lap)


def rectangle_area(bottom_left, top_right):
    return (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])


def line_over_lap_len(line1, line2):
    if line2[0] <= line1[0] <= line2[1]:
        return min(line2[1], line1[1]) - line1[0]
    elif line1[0] <= line2[0] <= line1[1]:
        return min(line2[1], line1[1]) - line2[0]
    else:
        return 0


if __name__ == '__main__':
    print(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
