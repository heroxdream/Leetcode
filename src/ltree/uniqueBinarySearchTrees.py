__author__ = 'hanxuan'


"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


def numTrees(n):
    """
    :param n:
    :return:
    """

    return numTreesRecursive(0, n, {})


def numTreesRecursive(startN, endN, d):
    """
    :param startN:
    :param endN:
    :return:
    """
    if (startN, endN) in d:
        return d[(startN, endN)]

    if endN - startN <= 1:
        d[(startN, endN)] = 1
        return d[(startN, endN)]

    ans = 0
    for i in range(startN, endN):
        ans += numTreesRecursive(startN, i, d) * numTreesRecursive(i + 1, endN, d)
    d[(startN, endN)] = ans

    return ans


if __name__ == '__main__':
    print(numTrees(2))
    print(numTrees(5))
    print(numTrees(10))
