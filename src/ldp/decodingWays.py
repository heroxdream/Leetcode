__author__ = 'hanxuan'
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

def numDecodings(s):
    """
    :param s:
    :return:
    """

    if not s:
        return 0

    if s[0] == '0':
        return 0

    for i in range(0, len(s)):
        if s[i - 1] == s[i] == '0':
            return 0
    d = {}
    re = decoding(s, d)
    # print(d)
    return re


def decoding(s, seen):

    if s in seen:
        return seen[s]

    if len(s) == 1:
        seen[s] = 1 if s != '0' else 0
        return seen[s]

    s0 = int(s[0])
    s1 = int(s[1])
    s0s1 = s0 * 10 + s1

    if len(s) == 2:
        if s0 > 2 and s1 == 0:
            seen[s] = 0
        elif s0s1 > 26 or s0s1 == 10:
            seen[s] = 1
        elif s1 == 0:
            seen[s] = 1
        else:
            seen[s] = 2
        return seen[s]

    if s0s1 == 10 or s0s1 == 20:
        seen[s] = decoding(s[2:], seen)
    elif s0s1 > 26 and s1 != 0:
        seen[s] = decoding(s[1:], seen)
    elif s0 > 2 and s1 == 0:
        seen[s] = 0
    else:
        seen[s] = decoding(s[1:], seen) + decoding(s[2:], seen)

    return seen[s]


def numDecodings_v2(s):
    """
    :param s:
    :return:
    """
    if not s:
        return 0
    d = {}
    re = decoding_v2(s, d)
    # print(d)
    return re


def decoding_v2(s, seen):

    if s in seen:
        return seen[s]

    if not s:
        seen[s] = 1
        return seen[s]

    if len(s) == 1:
        seen[s] = 1 if s != '0' else 0
        return seen[s]

    s0 = int(s[0])
    s1 = int(s[1])
    if s0 == 0:
        seen[s] = 0
        return seen[s]

    if s1 == 0 and s0 > 2:
        seen[s] = 0
        return seen[s]

    if s0 * 10 + s1 <= 26:
        seen[s] = decoding_v2(s[1:], seen) + decoding_v2(s[2:], seen)
    else:
        seen[s] = decoding_v2(s[1:], seen)

    return seen[s]



if __name__ == '__main__':

    print(numDecodings(''))         # 0
    print(numDecodings('01'))       # 0
    print(numDecodings('12'))       # 2
    print(numDecodings('123'))      # 3
    print(numDecodings('1322'))     # 4
    print(numDecodings('10'))       # 1
    print(numDecodings('10000001')) # 0
    print(numDecodings('909'))      # 0
    print(numDecodings('991829043812093481093'))    # 0
    print(numDecodings('390'))      # 0
    print(numDecodings('12120'))    # 3
    print(numDecodings('301'))    # 0
    print('############')
    print(numDecodings_v2(''))         # 0
    print(numDecodings_v2('01'))       # 0
    print(numDecodings_v2('12'))       # 2
    print(numDecodings_v2('123'))      # 3
    print(numDecodings_v2('1322'))     # 4
    print(numDecodings_v2('10'))       # 1
    print(numDecodings_v2('10000001')) # 0
    print(numDecodings_v2('909'))      # 0
    print(numDecodings_v2('991829043812093481093'))    # 0
    print(numDecodings_v2('390'))      # 0
    print(numDecodings_v2('12120'))    # 3
    print(numDecodings_v2('301'))    # 0
