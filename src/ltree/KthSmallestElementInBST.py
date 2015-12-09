"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
"""


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    nodeLeftCount = countNode(root.left)
    if k <= nodeLeftCount:
        return kthSmallest(root.left, k)
    elif k > nodeLeftCount + 1:
        return kthSmallest(root.right, k - nodeLeftCount - 1)
    else:
        return root.val


def countNode(root):
    if not root:
        return 0
    return 1 + countNode(root.left) + countNode(root.right)