__author__ = 'hanxuan'
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:
    1
   / \
  2   2
   \   \
   3    3

"""

from ltree.TreeNode import TreeNode

def isSymmetric(root):
    """
    :param root: TreeNode
    :return: bool
    """

    if root is None:
        return True

    pre_vals = []
    pre_order_traverse(root, pre_vals)

    if len(pre_vals) % 2 == 0:
        return False

    pos_vals = []
    post_order_traverse(root, pos_vals)

    in_vals = []
    in_order_traverse(root, in_vals)

    return pre_vals == pos_vals[::-1] and in_vals == in_vals[::-1]

def pre_order_traverse(root, vals):
    if root:
        vals.append(root.val)
        pre_order_traverse(root.left, vals)
        pre_order_traverse(root.right, vals)

def post_order_traverse(root, vals):
    if root:
        post_order_traverse(root.left, vals)
        post_order_traverse(root.right, vals)
        vals.append(root.val)

def in_order_traverse(root, vals):
    if root:
        in_order_traverse(root.left, vals)
        vals.append(root.val)
        in_order_traverse(root.right, vals)

def isSymmetricV2(root):
    if root is None:
        return True

    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False
    return True

def isSymmetricV3(root):
    return True if root is None else isMirror(root.left, root.right)

def isMirror(left, right):

    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val == right.val:
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    else:
        return False


if __name__ == '__main__':
    # root = TreeNode.build_tree_from_array([1, 2, 2, 3, 4, 4, 3])
    # TreeNode.traverse(root)
    print(isSymmetric(TreeNode.build_tree_from_array([1, 2, 2, 3, 4, 4, 3])))
    print(isSymmetric(TreeNode.build_tree_from_array([1, 2, 2, '#', 4, 4, '#'])))
    print(isSymmetric(TreeNode.build_tree_from_array([1, 2, 3, 3, '#', 2, '#'])))

    print(isSymmetricV3(TreeNode.build_tree_from_array([1, 2, 2, 3, 4, 4, 3])))
    print(isSymmetricV3(TreeNode.build_tree_from_array([1, 2, 2, '#', 4, 4, '#'])))
    print(isSymmetricV3(TreeNode.build_tree_from_array([1, 2, 3, 3, '#', 2, '#'])))

    print(isSymmetricV2(TreeNode.build_tree_from_array([1, 2, 2, 3, 4, 4, 3])))
    print(isSymmetricV2(TreeNode.build_tree_from_array([1, 2, 2, '#', 4, 4, '#'])))
    print(isSymmetricV2(TreeNode.build_tree_from_array([1, 2, 3, 3, '#', 2, '#'])))


