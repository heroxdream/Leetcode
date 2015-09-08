__author__ = 'hanxuan'


"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


def letter_combinations(digits):
    """
    :param digits:
    :return:
    """
    digits = ''.join([d for d in digits if d is not '1'])

    if len(digits) == 0:
        return []

    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    re = [[c] for c in d[digits[0]]]
    print(re)
    for i in range(1, len(digits)):
        s = d[digits[i]]
        tmp = []
        for l in re:
            for c in s:
                tl = l[:]
                tl.append(c)
                tmp.append(tl)
        re = tmp

    return [s for s in map(lambda x: ''.join(x), re)]


if __name__ == '__main__':
    print(letter_combinations('23'))
