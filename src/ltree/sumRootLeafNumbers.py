__author__ = 'hanxuan'


"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

def sumNumbers(root):
    """
    :param root:
    :return:
    """
    if not root:
        return 0

    return r(root, 0)

def r(root, p_value):
    """
    """

    value = p_value * 10 + root.val

    if (not root.left) and (not root.right):
        return value

    ans = 0
    if root.left:
        ans += r(root.left, value)
    if root.right:
        ans += r(root.right, value)

    return ans


from ltree.TreeNode import TreeNode

if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array([1, 2, 3, 4, 5])
    print(sumNumbers(r0))

    r1 = TreeNode.build_tree_from_array([0, 1, '#'])
    print(sumNumbers(r1))
