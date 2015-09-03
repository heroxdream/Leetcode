__author__ = 'hanxuan'

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant
 of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4
is 2, since a node can be a descendant of itself according to the LCA definition.
"""

def lowestCommonAncestor(root, p, q):
    """
    :param root: TreeNode
    :param p: TreeNode
    :param q: TreeNode
    :return: TreeNode
    """

    if p.val > q.val:
        return lowestCommonAncestor(root, q, p)

    if root is None:
        return None

    if p.val <= root.val <= q.val:
        return root
    elif root.val < p.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return lowestCommonAncestor(root.left, p, q)
