__author__ = 'hanxuan'

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""


def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """

    re = []
    seq = [0] * n
    seen = set()

    recursive(seq, seen, re)

    re2 = []
    for l in re:
        re2.append(b2d(l))

    return re2



def recursive(seq, seen, result):

    """
    :param listn:
    :param seen:
    :param result:
    :return:
    """

    identity = b2d(seq)
    if b2d(seq) in seen:
        return
    else:
        seen.add(identity)

    result.append(seq)
    for i in range(0, len(seq)):
        seq_new = seq[:]
        seq_new[i] = 0 if seq_new[i] == 1 else 1
        recursive(seq_new, seen, result)


def b2d(seq):
    """
    :param seq:
    :return:
    """

    result = 0
    for i in range(0, len(seq)):
        result += seq[i] * pow(2, i)
    return result


if __name__ == '__main__':

    # seq = [1, 1, 1]
    # print(b2d(seq))

    print(grayCode(2))
    print(grayCode(3))

