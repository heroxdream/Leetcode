__author__ = 'hanxuan'


"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""


def multiply(num1, num2):
    """
    :param num1: string
    :param num2: string
    :return: string
    """

    if num1.find('.') == -1:
        num1 += '.0'

    if num2.find('.') == -1:
        num2 += '.0'

    return multiply_decimal(num1, num2)


def multiply_decimal(n1, n2):
    """
    :param n1: string
    :param n2: string
    :return: string
    """
    a1, d1 = str2array(n1)
    a2, d2 = str2array(n2)
    re = multiply_array(a1, a2)
    re.insert(len(re) - d1 - d2, '.')
    return str(''.join(map(lambda x: str(x), re)))


def str2array(s):
    """
    :param s: string
    :return: (List[int], int)
    """
    re = [int(c) for c in s if c is not '.']
    len_after_decimal = len(s) - 1 - s.index('.')
    return re, len_after_decimal


def multiply_array(a1, a2):
    """
    :param a1: List[int]
    :param a2: List[int]
    :return: List[int]
    """

    l1 = len(a1)
    l2 = len(a2)

    result = [0] * (l1 + l2)
    for i in range(l1):
        for j in range(l2):
            m = str(a1[i] * a2[j])
            p = l1 - 1 - i + l2 - 1 - j
            add_array(result, m, p)
    return result


def add_array(long, short, p):
    """
    :param long: List[int]
    :param short: string
    :return: void
    """
    p1 = len(short) - 1
    p2 = len(long) - 1 - p
    carry = 0
    while p1 >= 0:
        re = long[p2] + int(short[p1]) + carry
        carry = 0
        if re >= 10:
            re %= 10
            carry = 1
        long[p2] = re
        p1 -= 1
        p2 -= 1

    while p2 >= 0:
        re = long[p2] + carry
        carry = 0
        if re >= 10:
            re %= 10
            carry = 1
        long[p2] = re
        p2 -= 1

    if carry == 1:
        long[p2] += 1


def multiply_v2(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product)-1

    for n1 in reversed(num1):
        tempPos = pos
        for n2 in reversed(num2):
            product[tempPos] += int(n1) * int(n2)
            product[tempPos-1] += product[tempPos] // 10
            product[tempPos] %= 10
            tempPos -= 1
        pos -= 1

    pt = 0
    while pt < len(product)-1 and product[pt] == 0:
        pt += 1

    return ''.join(map(str, product[pt:]))


if __name__ == '__main__':
    # a1 = [9, 9, 9]
    # a2 = [8, 8, 8]
    # print(multiply_array(a1, a1))
    #
    # a3 = [9, 9, 9, 9]
    # print(multiply_array(a3, a3))

    # d1 = '999.0'
    # d2 = '0.1'
    # print(multiply_decimal(d1, d1))
    # print(multiply_decimal(d1, d2))
    # print(multiply_decimal(d2, d2))

    s1 = '123'
    s2 = '456'
    print(multiply(s1, s1))
    print(multiply(s1, s2))
    print(multiply(s2, s2))

    from time import time

    t1 = time()
    s3, s4 = "17849419788197", "877968504004372811"
    # print(multiply(s3, s4))
    print(multiply_v2(s3, s4))

    t2 = time()
    s5, s6 = "4251760288481937956", "765115951945318380788262319277966797284599232062230077200"
    # print(multiply(s5, s6))
    print(multiply_v2(s5, s6))

    t3 = time()
    s7, s8 = "2322267896718392316129976729818262698599361122", "7348839706916210946024927859077721504476398931"
    # print(multiply(s7, s8))
    print(multiply_v2(s7, s8))

    t4 = time()
    s9, s10 = "6964594125027226699998128707627435007621143975736747759751", "333791918659904899647584436187733004125181" \
                                                                            "273682766434"
    # print(multiply(s9, s10))
    print(multiply_v2(s9, s10))

    t5 = time()
    s11, s12 = "32004015305", "8618149966947423286516878141192165991107723667986767544378680818317449411999708576220857" \
                              "81782887154570889788"
    # print(multiply(s11, s12))
    print(multiply_v2(s11, s12))

    t6 = time()

    print(t2 - t1)
    print(t3 - t2)
    print(t4 - t3)
    print(t5 - t4)
    print(t6 - t5)
