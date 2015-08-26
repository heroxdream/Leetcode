__author__ = 'hanxuan'

import sys

def reverseInteger(x):

    sx = str(x)
    sign = ''
    if sx[0] == '+' or sx[0] == '-':
        sign = sx[0]
        sx = sx[1:]
    sx = sx[::-1]
    xx = int(sign + ''.join(sx))

    if xx > pow(2, 31) - 1 or xx < -pow(2, 31):
        return 0
    else:
        return xx

def reverseIntegerV2(x):
    xx = (-1 if x < 0 else 1) * int(str(abs(x))[::-1])
    return 0 if (xx > pow(2, 31) - 1 or xx < -pow(2, 31)) else xx

if __name__ == '__main__':
    # print(reverseInteger(-12))
    # print(reverseInteger(12))
    # print(reverseInteger(1534236469))
    # print(reverseInteger(1000))

    print(reverseIntegerV2(-12))
    print(reverseIntegerV2(12))
    print(reverseIntegerV2(1534236469))
    print(reverseIntegerV2(1000))
