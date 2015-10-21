__author__ = 'hanxuan'


"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


from ltree.TreeNode import TreeNode

def inorderTraversal(root):
    """
    :param root:
    :return:
    """

    result = []
    recursive(root, result)
    return result


def recursive(root, result):

    if not root:
        return

    recursive(root.left, result)
    result.append(root.val)
    recursive(root.right, result)


def inorderTraversalIter(root):

    ans = []
    stack = []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            ans.append(node.val)
            root = node.right
    return ans


if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array(['1', '#', '2', '3', '#'])
    # TreeNode.traverse(r0)
    print(inorderTraversalIter(r0))
