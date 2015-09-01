__author__ = 'hanxuan'

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

from ltree.TreeNode import TreeNode

def minDepth(root):
    """
    :param root: TreeNode
    :return: int
    """

    if root is None:
        return 0

    if root.left is None and root.right is None:   # leaf
        return 1

    if root.left is None:
        return 1 + minDepth(root.right)

    if root.right is None:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))
