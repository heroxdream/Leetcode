__author__ = 'hanxuan'


"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """

    d = {}
    for i in range(len(s) - 10 + 1):
        sub = s[i:i+10]
        if sub not in d:
            d[sub] = 1
        else:
            d[sub] +=1

    ans= []
    for s in d:
        if d[s] > 1:
            ans.append(s)
    return ans