__author__ = 'hanxuan'


"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
s = 'aacc', t = 'aaac', return false
s = 'aa', t = 'a', return false

Note:
You may assume the string contains only lowercase alphabets.
"""

def isAnagram(s, t):
    """
    :param s: string
    :param t: string
    :return: bool
    """

    return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(isAnagram('a', 'b'))
