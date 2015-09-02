__author__ = 'hanxuan'
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

def isIsomorphic(s, t):
    """
    :param s: string
    :param t: string
    :return: bool
    """

    color1 = str2int(s)
    color2 = str2int(t)
    return color1 == color2


def str2int(s):
    n = 0
    color = [None] * len(s)
    color_map = {}
    for i in range(len(s)):
        if s[i] not in color_map:
            color_map[s[i]] = n
            n += 1
        color[i] = str(color_map[s[i]])
    return ''.join(color)

if __name__ == '__main__':
    print(isIsomorphic('paper', 'title'))
    print(isIsomorphic('egg', 'add'))
    print(isIsomorphic('', ''))