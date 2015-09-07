__author__ = 'hanxuan'


"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;

I   placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)

X   placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a
    hundred)

C   placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine
    hundred is CM (a hundred less than a thousand)
"""

def intToRoman(num):
    """
    :param num: int
    :return: string
    """
    result = ''

    if num >= 1000:
        m_count = num // 1000
        result += 'M' * m_count
        num -= 1000 * m_count

    if num >= 900:
        result += 'CM'
        num -= 900

    if num >= 500:
        result += 'D'
        num -= 500

    if num >= 400:
        result += 'CD'
        num -= 400

    if num >= 100:
        c_count = num // 100
        result += 'C' * c_count
        num -= 100 * c_count

    if num >= 90:
        result += 'XC'
        num -= 90

    if num >= 50:
        result += 'L'
        num -= 50

    if num >= 40:
        result += 'XL'
        num -= 40

    if num >= 10:
        x_count = num // 10
        result += 'X' * x_count
        num -= 10 * x_count

    if num >= 9:
        result += 'IX'
        num -= 9

    if num >= 5:
        result += 'V'
        num -= 5

    if num >= 4:
        result += 'IV'
        num -= 4

    if num >= 1:
        i_count = num
        result += 'I' * i_count

    return result


if __name__ == '__main__':
    print(intToRoman(1))
    print(intToRoman(4))
    print(intToRoman(5))
    print(intToRoman(9))
    print(intToRoman(1954))
    print(intToRoman(1990))
    print(intToRoman(2014))
