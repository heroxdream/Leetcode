__author__ = 'hanxuan'


"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


def generate_parenthesis(n):
    """
    :param n: int
    :return: List[string]
    """
    if n == 0:
        return []

    re = recursive_generate(n, n, 0)
    return [s for s in map(lambda x: ''.join(x), re)]


def recursive_generate(pos, neg, sm):
    """
    :param pos: int >= 0
    :param neg: int >= 0
    :param sm: int >= 0
    :return: List[List[string]]
    """

    if pos == 0 and neg == 1:
        return [[')']]

    if sm == 0:
        re = []
        curr = '('
        sub = recursive_generate(pos - 1, neg, sm + 1)
        for l in sub:
            l.insert(0, curr)
            re.append(l)
        return re

    if sm > 0:
        re = []
        if pos > 0:
            curr1 = '('
            sub1 = recursive_generate(pos - 1, neg, sm + 1)
            for l in sub1:
                l.insert(0, curr1)
                re.append(l)

        curr2 = ')'
        sub2 = recursive_generate(pos, neg - 1, sm - 1)
        for l in sub2:
            l.insert(0, curr2)
            re.append(l)
        return re


if __name__ == '__main__':
    print(generate_parenthesis(0))
    print(generate_parenthesis(1))
    print(generate_parenthesis(2))
    print(generate_parenthesis(3))
