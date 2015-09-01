__author__ = 'hanxuan'
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from ltree.TreeNode import TreeNode

def levelOrder(root):
    """
    :param root: TreeNode
    :return: List[List[int]]
    """

    result = []
    if root is None:
        return result

    stack = [root]
    while stack:
        tmp = []
        level = []
        for node in stack:
            tmp.append(node.left) if node.left else 0
            tmp.append(node.right) if node.right else 0
            level.append(node.val)

        result.append(level)
        stack = tmp

    return result

if __name__ == '__main__':
    print(levelOrder(TreeNode.build_tree_from_array([1])))
    print(levelOrder(TreeNode.build_tree_from_array([])))
    print(levelOrder(TreeNode.build_tree_from_array([3, 9, 20, '#', '#', 15, 7])))
    print(levelOrder(TreeNode.build_tree_from_array([1, '#', 2, 3, '#'])))
