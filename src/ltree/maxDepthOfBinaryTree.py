__author__ = 'hanxuan'

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from ltree.TreeNode import TreeNode

def maxDepth(root):
    """
    :param root: TreeNode
    :return: int
    """

    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


