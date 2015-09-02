__author__ = 'hanxuan'
"""
Write a function that takes an unsigned integer and returns the number of ’1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""

def hammingWeight(n):

    return sum(map(lambda x: int(x), '{:b}'.format(n)))

def hammingWeightV2(n):

    result = 0
    while True:
        result += n % 2
        n >>= 1
        if n == 0:
            break

    return result


if __name__ == '__main__':
    print(hammingWeight(3))
    print(hammingWeightV2(3))