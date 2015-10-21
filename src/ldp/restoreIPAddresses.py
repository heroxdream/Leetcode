__author__ = 'hanxuan'

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


def restoreIpAddresses(s):
    """
    :param s:
    :return:
    """
    if not s:
        return []
    else:
        return restore(s, 3)

def restore(s, cut):

    """
    :param s:
    :return:
    """

    if len(s) - cut < 1:
        return []

    if cut == 0 and s2n(s) > 255:
        return []

    if cut == 0 and len(s) >1 and s[0] == '0':
        return []

    if cut == 0:
        return [s]

    if len(s) == 1:
        return [s]

    re = []
    for i in range(3):

        if i > len(s) - 1:
            break

        head = s[0:i + 1]
        if i >= 1 and s[0] == '0':
            continue
        if s2n(head) > 255:
            continue

        rest = restore(s[i + 1:], cut - 1)
        for l in rest:
            re.append(head + '.' + l)

    return re

def s2n(s):
    re = 0
    for i in range(len(s)):
        re += int(s[i]) * pow(10, len(s) - 1 - i)
    return re

if __name__ == '__main__':
    s0 = '0000'
    s1 = '25525511135'
    s2 = '21001001'
    print(restoreIpAddresses(s0))
    print(restoreIpAddresses(s1))
    print(restoreIpAddresses(s2))




