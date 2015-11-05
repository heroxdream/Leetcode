__author__ = 'hanxuan'


"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""


def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = []
    r(root, ans, 0)
    return ans

def r(root, ans, depth):

    if not root:
        return

    if depth == len(ans):
        ans.append(root.val)

    r(root.right, ans, depth + 1)
    r(root.left, ans, depth + 1)
