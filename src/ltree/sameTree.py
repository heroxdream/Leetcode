__author__ = 'hanxuan'
"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

from ltree.TreeNode import TreeNode

def isSameTree(p, q):
    """
    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """

    if p is None and q is None:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(q.right, q.right)
    else:
        return False



