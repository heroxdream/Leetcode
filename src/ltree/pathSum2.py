__author__ = 'hanxuan'


"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


def pathSum(root, sum):
    """
    :param root:
    :param sum:
    :return:
    """
    if not root:
        return []

    if not root.right and not root.left:
        return [] if sum != root.val else [[root.val]]

    ans_left = pathSum(root.left, sum - root.val)
    ans_right = pathSum(root.right, sum - root.val)

    ans = []
    for l in ans_left + ans_right:
        l.insert(0, root.val)
        ans.append(l)

    return ans


from ltree.TreeNode import TreeNode

if __name__ == '__main__':
    r0 = TreeNode.build_tree_from_array([1, 2, '#'])
    print(pathSum(r0, 3))
