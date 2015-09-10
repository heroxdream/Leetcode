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

    candidates = sorted(set(candidates))
    d = {}
    return recursive_combine(candidates, 0, target, d)


def recursive_combine(candidates, idx, target, d):
    if (idx, target) in d:
        return d[(idx, target)]

    if idx == len(candidates) - 1:
        re = [[candidates[idx]] * (target // candidates[idx])] if target % candidates[idx] == 0 else []
        d[(idx, target)] = re
        return re

    re = []
    x, y = target // candidates[idx], candidates[idx]
    for i in range(x + 1):
        curr = [y] * i
        sub = recursive_combine(candidates, idx + 1, target - y * i, d)
        for l in sub:
            re.append(curr + l)
    d[(idx, target)] = re
    return re


def combination_sum_v2(candidates, target):
    """
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """

    if len(candidates) == 0:
        return []

    coefficients = dict([(i, 0) for i in candidates])
    for c in candidates:
        coefficients[c] += 1
    d = {}
    candidates = sorted(set(candidates))
    return recursive_combine_v2(candidates, coefficients, 0, target, d)


def recursive_combine_v2(candidates, coefficients, idx, target, d):

    print('recursive_combine_v2 begin', candidates, coefficients, idx, target, d)

    if (idx, target) in d:
        return d[(idx, target)]

    if target == 0:
        d[(idx, target)] = [[]]
        return [[]]

    y = candidates[idx]
    if idx == len(candidates) - 1:
        x = coefficients[y]
        d[(idx, target)] = [[y] * (target // y)] if y <= target <= y * x and target % y == 0 else []
        return d[(idx, target)]

    re = []
    if y > target:
        d[(idx, target)] = []
        return []
    x = max(coefficients[y], min(1, target // y))
    for i in range(x + 1):
        curr = [y] * i
        sub = recursive_combine_v2(candidates, coefficients, idx + 1, target - y * i, d)
        re += [(curr + l) for l in sub]
    d[(idx, target)] = re
    return re

if __name__ == '__main__':
    # n0 = [1, 2, 3]
    # print(combination_sum(n0, 6))
    #
    # n1, t1 = [2], 1
    # print(combination_sum(n1, t1))
    #
    # n2, t3 = [8, 7, 4, 3], 11
    # print(combination_sum(n2, t3))

    n3, t3 = [1, 2, 2], 4
    # print(combination_sum(n3, t3))
    print(combination_sum_v2(n3, t3))

    n4, t4 = [1, 1, 1, 1, 1, 1], 2
    # print(combination_sum(n4, t4))
    print(combination_sum_v2(n4, t4))

    n4, t4 = [2], 1
    # print(combination_sum(n4, t4))
    print(combination_sum_v2(n4, t4))

    # from time import time
    # t1 = time()
    # n5, t5 = [22,21,18,18,23,14,26,14,34,8,33,29,32,14,6,32,34,22,25,14,25,31,9,7,20,31,34,32,18,34,8,27,13,21,10,31,22,24,10,13,27,8,7,16,10,30,5,9,17,26,11,8,22,7], 25
    # print(combination_sum_v2(n5, t5))
    # t2 = time()
    # n6, t6 = [8,26,25,10,20,27,27,20,24,25,20,13,28,16,32,31,34,12,21,29,26,11,14,34,7,22,28,22,25,25,15,20,17,27,17,24,19,10,9,30,22,17,30,15,28,27,33,19,26,20,6], 23
    # print(combination_sum_v2(n6, t6))
    # t3 = time()
    #
    # print(t2 - t1)
    # print(t3 - t2)

    n7, t7 = [4, 4, 2, 1, 4, 2, 2, 1, 3], 6
    print(combination_sum_v2(n7, t7))
