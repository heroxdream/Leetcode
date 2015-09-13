__author__ = 'hanxuan'


"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


def my_sqrt(n):
    """
    :param n: int
    :return: int
    """
    return binary_search_sqrt(0, n, n)

def binary_search_sqrt(l, r, n):
    """
    :param l:
    :param r:
    :param n:
    :return:
    """
    if l > r:
        return r

    mid = (l + r) // 2
    if mid ** 2 == n:
        return mid

    elif mid ** 2 > n:
        return binary_search_sqrt(l, mid - 1, n)
    else:
        return binary_search_sqrt(mid + 1, r, n)


if __name__ == '__main__':
    print(my_sqrt(0))
    print(my_sqrt(1))
    print(my_sqrt(2))
    print(my_sqrt(4))
    print(my_sqrt(7))
    print(my_sqrt(10))
    print(my_sqrt(100))
