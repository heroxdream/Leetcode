__author__ = 'hanxuan'


"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

def divide(dividend, divisor):
    """
    :param dividend: int
    :param divisor: int
    :return: int
    """

    if (dividend == -2147483648 and divisor == -1) or divisor == 0:
        return 2147483647

    sign = 1 if (dividend > 0) is (divisor > 0) else -1

    dividend, divisor = abs(dividend), abs(divisor)
    ans = 0
    while dividend > 0:
        x = divisor
        an = 1 if dividend >= x else 0
        while dividend >= x:
            an <<= 1
            x <<= 1

        an >>= 1
        x >>= 1
        dividend -= x
        ans += an
    return ans * sign


if __name__ == '__main__':
    print(divide(5, 2))
    print(divide(15, -3))

