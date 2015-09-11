__author__ = 'hanxuan'


"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""


def group_anagrams(strs):
    """
    :param strs: List[str]
    :return: List[List[str]]
    O(n ^ 2) time O(n) space
    """

    d = {}
    for s in strs:
        key = stat_hash(s)
        if key not in d:
            d[key] = []
        d[key].append(s)

    return [sorted(l) for l in d.values()]


def stat_hash(s):
    """
    :param s: string which len(s) >= 0
    :return: int
    """
    if len(s) == 0:
        return 0.5

    counter = 0
    record = []
    ss = sorted(s)
    last_c = ss[0]
    for c in ss:
        counter += 1
        if last_c is not c:
            record.append(last_c)
            record.append(str(counter))
            last_c = c
            counter = 0
    record.append(last_c)
    record.append(str(counter))
    print(record)
    return hash(''.join(record))


def group_anagrams_v2(strs):
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in d:
            d[key] = []
        d[key].append(s)
    return [sorted(l) for l in d.values()]


if __name__ == '__main__':
    s0 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(stat_hash(s0[0]), stat_hash(s0[1]))
    print(group_anagrams(s0))

    s1 = ["ape", "and", "cat", '', '']
    print(group_anagrams(s1))

    s2 = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
    print(group_anagrams(s2))

    print(stat_hash('max'), stat_hash('may'))

    print(group_anagrams_v2(s1))
    print(group_anagrams_v2(s2))
    print(group_anagrams_v2(s0))
