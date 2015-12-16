"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    table1 = {}

    label = 0
    for s in pattern:
        if s not in table1:
            table1[s] = label
            label += 1

    encode1 = []
    for s in pattern: encode1.append(table1[s])

    table2 = {}
    label2 = 0
    for ss in str.split(' '):
        if ss not in table2:
            table2[ss] = label2
            label2 += 1
    encode2 = []
    for ss in str.split(' '): encode2.append(table2[ss])

    if len(encode1) != len(encode2):
        return False

    for i in range(len(encode1)):
        if encode1[i] != encode2[i]:
            return False

    return True
