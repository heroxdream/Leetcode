__author__ = 'hanxuan'
def atoi(sx):
    import re

    MAX_INT = pow(2, 31) - 1
    MIN_INT = - pow(2, 31)

    sx = sx.strip()
    valid_sx = re.findall('(^\+|\-\d*)\D*', sx)
    print(valid_sx)
    try:
        result = int(''.join(valid_sx))
        return result if result in range(MIN_INT, MAX_INT + 1) else MAX_INT if result > MAX_INT else MIN_INT
    except:
        return 0

if __name__ == '__main__':
    print(atoi('+-1'))