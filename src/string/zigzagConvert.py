__author__ = 'hanxuan'

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows <= 1 or numRows >= len(s):
        return s

    zig = numRows
    zag = numRows - 2

    array = []
    for i in range(0, len(s), zig + zag):
        array.append(s[i])

    for i in range(1, numRows - 1):
        idx = i
        while True:
            array.append(s[idx])
            idx += zig + zag - 2 * i
            if idx >= len(s):
                break
            array.append(s[idx])
            idx += 2 * i
            if idx >= len(s):
                break

    for i in range(numRows - 1, len(s), zig + zag):
        array.append(s[i])

    return ''.join(array)

if __name__ == '__main__':
    s0 = 'abc'
    s1 = 'PAYPALISHIRING'

    print(convert(s0, 1))
    print(convert(s0, 2))
    print(convert(s0, 3))

    print(convert(s1, 1))
    print(convert(s1, 2))
    print(convert(s1, 3))
