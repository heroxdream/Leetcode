__author__ = 'hanxuan'
def addBinaryV1(a, b):

    pointera = len(a) - 1
    pointerb = len(b) - 1
    carry = 0
    re = []
    while pointera >= 0 and pointerb >= 0:
        digit = carry + int(a[pointera]) + int(b[pointerb])
        carry = 0
        if digit >= 2:
            carry = 1
            digit %= 2
        re.append(digit)
        pointera -= 1
        pointerb -= 1

    while pointera >= 0:
        digit = carry + int(a[pointera])
        carry = 0
        if digit >= 2:
            carry = 1
            digit %= 2
        re.append(digit)
        pointera -= 1

    while pointerb >= 0:
        digit = carry + int(b[pointerb])
        carry = 0
        if digit >= 2:
            carry = 1
            digit %= 2
        re.append(digit)
        pointerb -= 1

    if carry == 1:
        re.append(1)

    return ''.join(map(lambda x: str(x), reversed(re)))

def addBinaryV2(a, b):

    if len(a) < len(b):
        return addBinaryV2(b, a)

    pointera = len(a) - 1
    pointerb = len(b) - 1
    carry = 0
    re = []
    while pointera >= 0 and pointerb >= 0:
        digit = carry + int(a[pointera]) + int(b[pointerb])
        carry = 0
        if digit >= 2:
            carry = 1
            digit %= 2
        re.append(digit)
        pointera -= 1
        pointerb -= 1

    while pointera >= 0:
        digit = carry + int(a[pointera])
        carry = 0
        if digit >= 2:
            carry = 1
            digit %= 2
        re.append(digit)
        pointera -= 1

    if carry == 1:
        re.append(1)

    return ''.join(map(lambda x: str(x), reversed(re)))

if __name__ == '__main__':
    print(addBinaryV1('0', '1'))
    print(addBinaryV1('101', '1'))
    print(addBinaryV1('1111', '1'))
    print(addBinaryV1('111', '1111'))

    print(addBinaryV2('0', '1'))
    print(addBinaryV2('101', '1'))
    print(addBinaryV2('1111', '1'))
    print(addBinaryV2('111', '1111'))
