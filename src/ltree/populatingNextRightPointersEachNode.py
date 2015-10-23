__author__ = 'hanxuan'


"""
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree
(ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

from ltree.TreeLinkNode import TreeLinkNode

def connect(root):
    """
    :param root:
    :return:
    """

    connect_recursive(root, None)


def connect_recursive(root, pal):
    """
    :param root:
    :param pal:
    :return:
    """

    if not root:
        return None

    root.next = pal
    new_pal = connect_recursive(root.right, None if not pal else pal.left)
    connect_recursive(root.left, new_pal)
    return root

if __name__ == '__main__':
    tl0 = TreeLinkNode.build_tree_from_array([1, 2, 3])
    connect(tl0)
    TreeLinkNode.traverse(tl0)
