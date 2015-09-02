__author__ = 'hanxuan'
"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
                 return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

def reverseBitsV1(n):
    return int('{:032b}'.format(n)[::-1], 2)


def reverseBitsV2(n):
    pointer = 31
    result = 0
    while pointer > 0:
        x = n % 2
        result += x * 2 ** pointer
        n >>= 1
        pointer -= 1

    return result

if __name__ == '__main__':
    print(reverseBitsV1(43261596))
    print(reverseBitsV2(43261596))
