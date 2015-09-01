__author__ = 'hanxuan'

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

def hasPathSum(root, sum):
    """
    :param root: TreeNode
    :param sum: int
    :return: bool
    """
    if root is None:
        return False

    if root.left is None and root.right is None:
        return True if sum == root.val else False

    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)