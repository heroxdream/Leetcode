__author__ = 'hanxuan'


"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

from ltree.TreeNode import TreeNode

def generateTrees(n):
    """
    :param n:
    :return:
    """
    if n < 1:
        return []

    ans = recursive(1, n, {})
    return ans

def recursive(startN, endN, d):
    """
    :param startN:
    :param endN:
    :param result:
    :return:
    """

    if (startN, endN) in d:
        return d[(startN, endN)]

    if endN - startN < 0:
        d[(startN, endN)] = [None]
        return d[(startN, endN)]

    if endN - startN == 0:
        d[(startN, endN)] = [TreeNode(startN)]
        return d[(startN, endN)]

    ans = []
    for i in range(startN, endN + 1):
        ansL = recursive(startN, i - 1, d)
        ansR = recursive(i + 1, endN, d)

        for nl in ansL:
            for nr in ansR:
                node = TreeNode(i)
                node.left = nl
                node.right = nr
                ans.append(node)

    return ans


if __name__ == '__main__':
    r0 = generateTrees(0)
    for t in r0:
        TreeNode.traverse(t)
