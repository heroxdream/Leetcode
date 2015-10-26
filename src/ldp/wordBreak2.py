__author__ = 'hanxuan'

"""
"""


def wordBreak(s, wordDict):
    """
    :param s:
    :param wordDict:
    :return:
    """

    if not s or not wordDict:
        return []

    return r(s, wordDict, {})

def r(s, d, dd):

    if s in dd:
        return dd[s]

    if not s:
        return ['']

    ans = []
    for i in range(1, len(s) + 1):
        if s[:i] in d:
            for l in r(s[i:], d, dd):
                l = s[:i] + ' ' + l
                ans.append(l.strip())

    dd[s] = ans
    return ans

if __name__ == '__main__':
    s0 = 'leetcode'
    d0 = ["leet", "code"]
    print(wordBreak(s0, d0))

    s1 = 'catsanddog'
    d1 = ["cat", "cats", "and", "sand", "dog"]
    print(wordBreak(s1, d1))
