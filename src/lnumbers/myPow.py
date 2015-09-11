__author__ = 'hanxuan'


"""
Implement pow(x, n).
"""


def my_pow(x, n):
    """
    :param x: float
    :param n: int
    :return: float
    """

    sign = 1 if n == abs(n) else -1
    n = abs(n)
    result = 1
    while n > 0:
        order = 1
        y = x
        while True:
            order *= 2
            if order > n:
                break
            y *= y
        result *= y
        n -= order // 2
    return result if sign > 0 else 1 / result

if __name__ == '__main__':

    print(my_pow(0, 0))
    print(my_pow(-3, 1))
    print(my_pow(-3, 2))
    print(my_pow(-2, 11))
    print(my_pow(2, -1))
