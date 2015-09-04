__author__ = 'hanxuan'


"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

from ltree.TreeNode import TreeNode

def binaryTreePaths(root):
    """
    :param root: TreeNode
    :return: List[string]
    """

    return [i for i in map(lambda x: '->'.join(x), helper(root))]


def helper(root):

    if root is None:
        return []

    left_routes = helper(root.left)
    right_routes = helper(root.right)

    combine = left_routes + right_routes

    if not combine:
        return [[str(root.val)]]

    for route in combine:
        route.insert(0, str(root.val))

    return combine

if __name__ == '__main__':

    t = TreeNode.build_tree_from_array([1, 2, 3, 4, '#', 5, 6])
    TreeNode.traverse(t)
    print(helper(t))
    print(binaryTreePaths(t))
