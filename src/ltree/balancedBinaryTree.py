__author__ = 'hanxuan'

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.
"""

from ltree.TreeNode import TreeNode

def isBalanced(root):
    """
    :param root: TreeNode
    :return: bool
    """
    if root is None:
        return True

    depth_record = {}
    return isBalanced(root.left) and isBalanced(root.right) \
        and abs(depth(root.left, depth_record) - depth(root.right, depth_record)) <= 1


def depth(root, depth_dict):
    """
    :param root: TreeNode
    :return: int
    """
    if root in depth_dict:
        return depth_dict[root]

    if root is None:
        depth_dict[root] = 0
        return 0

    depth_dict[root] = 1 + max(depth(root.left, depth_dict), depth(root.right, depth_dict))
    return depth_dict[root]


if __name__ == '__main__':
    print(isBalanced(TreeNode.build_tree_from_array([])))
    print(isBalanced(TreeNode.build_tree_from_array([1])))
    print(isBalanced(TreeNode.build_tree_from_array([1, '#', 3])))
    print(isBalanced(TreeNode.build_tree_from_array([1, 3, 3, '#', 2, '#', 3, 2, 3])))
