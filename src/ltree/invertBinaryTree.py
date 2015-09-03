__author__ = 'hanxuan'
"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


from ltree.TreeNode import TreeNode

def invertTree(root):

    if root is None:
        return root

    l = invertTree(root.left)
    r = invertTree(root.right)

    root.left = r
    root.right = l

    return root

if __name__ == '__main__':
    root = TreeNode.build_tree_from_array([1, 2, 3])
    TreeNode.traverse(root)

    new_root = invertTree(root)
    TreeNode.traverse(new_root)
