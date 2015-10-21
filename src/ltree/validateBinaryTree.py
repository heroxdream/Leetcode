__author__ = 'hanxuan'


"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


from ltree.TreeNode import TreeNode

def validate(root):
    """
    :param root:
    :return:
    """

    if not root:
        return True

    if not root.right and not root.left:
        return True

    value_root = root.val

    if maxVal(root.left) >= value_root:
        return False

    if minVal(root.right) <= value_root:
        return False

    return validate(root.left) and validate(root.right)


def maxVal(root):

    if not root:
        return -999999999999
    ans = max(root.val, maxVal(root.left), maxVal(root.right))
    return ans

def minVal(root):

    if not root:
        return 9999999999999
    ans = min(root.val, minVal(root.left), minVal(root.right))
    return ans




if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array([2, 1, 3])
    # TreeNode.traverse(r0)
    print(validate(r0))

    # print(maxVal(r0))
    # print(minVal(r0))
    r1 = TreeNode.build_tree_from_array([10, 5, 15, '#', '#', 6, 20])
    # TreeNode.traverse(r1)

    # print(maxVal(r1))
    # print(minVal(r1))
    print(validate(r1))

    r2 = TreeNode.build_tree_from_array([0, '#', 1])
    # TreeNode.traverse(r2)
    print(validate(r2))
