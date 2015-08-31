__author__ = 'hanxuan'

"""
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
"""

def plusOne(digits):
    """
    :param digits: List[int]
    :return: List[int]
    """
    carry = 1
    re = []
    for digit in reversed(digits):
        curr = digit + carry
        carry = 0
        if curr >= 2:
            carry = 1
            curr %= 2
        re.append(curr)
    if carry == 1:
        re.append(1)

    return [digit for digit in reversed(re)]

if __name__ == '__main__':
    print(plusOne([1,1,1]))
    print(plusOne([1]))
    print(plusOne([0]))

