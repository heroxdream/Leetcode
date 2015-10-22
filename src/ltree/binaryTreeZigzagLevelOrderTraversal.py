__author__ = 'hanxuan'


"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

def zigzagLevelOrder(root):
    """
    :param root:
    :return:
    """

    if not root:
        return []

    ans = []
    current_layer = [root]
    reverse = False

    while current_layer:
        new_layer = []
        result_current_layer = []
        for node in current_layer:
            result_current_layer.append(node.val)
            if node.left:
                new_layer.append(node.left)
            if node.right:
                new_layer.append(node.right)
        if reverse:
            result_current_layer.reverse()
            reverse = False
        else:
            reverse = True
        ans.append(result_current_layer)

        current_layer = new_layer

    return ans


from ltree.TreeNode import TreeNode

if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array([])
    r1 = TreeNode.build_tree_from_array([1])
    r2 = TreeNode.build_tree_from_array([3, 9, 20, '#', '#', 15, 7])

    ans0 = zigzagLevelOrder(r0)
    print(ans0)

    ans1 = zigzagLevelOrder(r1)
    print(ans1)

    ans2 = zigzagLevelOrder(r2)
    print(ans2)



