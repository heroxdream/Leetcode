__author__ = 'hanxuan'


"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C
where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

def combination_sum(candidates, target):
    """
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """

    if len(candidates) == 0:
        return []

    candidates = sorted(candidates)
    d = {}
    return recursive_combine(candidates, 0, target, d)

def recursive_combine(candidates, idx, target, d):
    if (idx, target) in d:
        return d[(idx, target)]

    if idx == len(candidates) - 1:
        return [[candidates[idx]] * (target // candidates[idx])] if target % candidates[idx] == 0 else []

    re = []
    x, y = target // candidates[idx], candidates[idx]
    for i in range(x + 1):
        curr = [y] * i
        sub = recursive_combine(candidates, idx + 1, target - y * i, d)
        for l in sub:
            re.append(curr + l)
    d[(idx, target)] = re
    return re


def spawn(a, start):
    """
    :param a: List[int]
    :return: List[List[int]]
    """
    if start == len(a) - 1:
        return [[a[start]]]

    sub = spawn(a, start + 1)
    re = [[a[start]]]
    for l in sub:
        re.append(l[:])
    for l in sub:
        l.insert(0, a[start])
        re.append(l)

    return re


if __name__ == '__main__':
    n0 = [1, 2, 3]
    print(combination_sum(n0, 6))

    n1, t1 = [2], 1
    print(combination_sum(n1, t1))

    n2, t3 = [8, 7, 4, 3], 11
    print(combination_sum(n2, t3))
