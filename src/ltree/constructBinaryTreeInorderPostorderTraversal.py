__author__ = 'hanxuan'


"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

from ltree.TreeNode import TreeNode

def buildTree(inorder, postorder):

    if inorder:
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.right = buildTree(inorder[ind+1:], postorder)
        root.left = buildTree(inorder[:ind], postorder)
        return root

    return None


def buildTree_v2(inorder, postorder):

    return build(inorder, postorder, 0, len(inorder), 0, len(postorder))

def build(inorder, postorder, inStart, inEnd, postStart, postEnd):

    # print(inStart, inEnd, postStart, postEnd)

    if inEnd - inStart == 0:
        return None

    if inEnd - inStart == 1:
        return TreeNode(postorder[postStart])

    root = TreeNode(postorder[postEnd - 1])

    left_in_set = set()
    pointer = inStart
    while inorder[pointer] != root.val:
        left_in_set.add(inorder[pointer])
        pointer += 1
    leftInEnd = pointer
    rightInStart = pointer + 1

    pointer = postStart
    while postorder[pointer] in left_in_set:
        pointer += 1
    leftPosEnd = pointer
    rightPosStart = pointer

    root.left = build(inorder, postorder, inStart, leftInEnd, postStart, leftPosEnd)
    root.right = build(inorder, postorder, rightInStart, inEnd, rightPosStart, postEnd - 1)

    return root



if __name__ == '__main__':
    i0 = [1, 2, 3, 4]
    p0 = [1, 2, 4, 3]
    r0 = buildTree_v2(i0, p0)
    TreeNode.traverse(r0)