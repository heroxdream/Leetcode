__author__ = 'hanxuan'

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of
one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

def wordBreak(s, wordDict):
    """
    :param s:
    :param wordDict:
    :return:
    """

    if not s or not wordDict:
        return False

    return r(s, wordDict, {})



def r(s, d, dd):

    if len(s) in dd:
        return dd[len(s)]

    if not s:
        return True

    for i in range(1, len(s) + 1):
        if s[:i] in d:
            if r(s[i:], d, dd):
                dd[len(s)] = True
                return dd[len(s)]

    dd[len(s)] = False
    return dd[len(s)]


if __name__ == '__main__':
    s0 = 'leetcode'
    d0 = ["leet", "coded"]
    print(wordBreak(s0, d0))

    s1 = 'aaaaaaa'
    d1 = ["aaaa", "aaa"]
    print(wordBreak(s1, d1))


