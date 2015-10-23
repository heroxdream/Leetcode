__author__ = 'hanxuan'

# Definition for binary tree with next pointer.

from ltree.TreeNode import TreeNode

class TreeLinkNode(TreeNode):
    def __init__(self, x):
        super(x)
        self.next = None

    @staticmethod
    def traverse(root):
        if root is None:
            print('none')
        else:
            print(root.val, root.next)
            TreeLinkNode.traverse(root.left)
            TreeLinkNode.traverse(root.right)
