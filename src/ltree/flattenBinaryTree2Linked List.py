__author__ = 'hanxuan'


"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""


def flatten(root):
    """
    :param root:
    :return:
    """

    if not root:
        return None

    left_root = flatten(root.left)
    right_root = flatten(root.right)

    root.left = None
    root.right = left_root

    end_pointer = root
    while left_root:
        end_pointer = left_root
        left_root = left_root.right

    end_pointer.right = right_root

    return root


from ltree.TreeNode import TreeNode
if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array([1,2,3,4,5,6,7])
    # TreeNode.traverse(r0)
    TreeNode.traverse(flatten(r0))
