__author__ = 'hanxuan'


"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""


# def partition(s):
#     """
#     :type s: str
#     :rtype: List[List[str]]
#     """
#     if not s:
#         return []
#
#     return r(s)
#
# def r(s):
#     if len(s) == 0:
#         return [[]]
#
#     c = s[0]
#     sub_result = r(s[1:])
#
#     new_result = []
#     for l in sub_result:
#         new_l = l[:]
#         if new_l == [] or c == new_l[-1]:
#             new_l.insert(0, c)
#             new_result.append(new_l)
#     return new_result


def partition(s):
    res = []
    cal(s, res, [])
    return res

def cal(s, res, temp):

    if not s:
        res.append(temp[:])
        return

    for i in range(len(s)):
        if s[: i+1] == s[: i+1][:: -1]:
            cal(s[i+1:], res, temp + [s[: i + 1]])

if __name__ == '__main__':
    print(partition(''))
    print(partition('a'))
    print(partition('aaaa'))
    print(partition('bc'))
    print(partition('aab'))
