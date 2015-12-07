"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last
level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""


def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if not root: return 0

    heightL = depth(root.left)
    heightR = depth(root.right)

    if heightL == heightR:
        return pow(2, heightL) + countNodes(root.right)
    else:
        return pow(2, heightR) + countNodes(root.left)


def depth(node):
    if not node:return 0
    return 1 + depth(node.left)

