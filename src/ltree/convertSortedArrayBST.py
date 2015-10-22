__author__ = 'hanxuan'



"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

from ltree.TreeNode import TreeNode


def sortedArrayToBST(nums):

    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return TreeNode(nums[0])

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[0: mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


if __name__ == '__main__':
    a0 = [1, 2, 3, 4, 5, 6, 7, 8]
    t0 = sortedArrayToBST(a0)
    TreeNode.traverse(t0)
