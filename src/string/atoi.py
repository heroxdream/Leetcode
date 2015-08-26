__author__ = 'hanxuan'
def atoi(sx):
    """
    :param sx: string
    :return: int

    lots of corner cases:
    '+1234'
    '-1234'
    '1234'
    '+1234abc'
    '   1234'
    '000123'
    ' - 0001234'
    '12341234123412341234123412341341'      too big
    '-12341234123412341234123412341341'     too small overflow

    """
    import re

    max_int = pow(2, 31) - 1
    min_int = - pow(2, 31)

    sx = sx.strip()
    valid_sx = re.findall('(^\+|\-\d*)\D*', sx)

    try:
        result = int(''.join(valid_sx))
        return result if result in range(min_int, max_int + 1) else max_int if result > max_int else min_int
    except Exception as e:
        print(e)
        return 0

if __name__ == '__main__':
    print(atoi('+-1'))
