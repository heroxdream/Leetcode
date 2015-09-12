__author__ = 'hanxuan'


"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


def get_permutation(n, k):
    """
    :param n:
    :param k:
    :return:
    """
    k -= 1
    l = [(i + 1) for i in range(n)]
    result = []
    while k >= 0:
        if k == 0:
            result += l
            break
        base = f(len(l) - 1)
        y = base
        for i in range(len(l)):
            if k < y:
                result.append(str(l[i]))
                l.pop(i)
                break
            y += base

        y -= base
        k -= y
    return ''.join(map(str, result))

def f(n):
    return 1 if n <= 1 else n * f(n - 1)


if __name__ == '__main__':
    # print(get_permutation(1, 1))
    print(get_permutation(3, 1))
    print(get_permutation(3, 2))
    print(get_permutation(3, 3))
    print(get_permutation(3, 4))
    print(get_permutation(3, 5))
    print(get_permutation(3, 6))
