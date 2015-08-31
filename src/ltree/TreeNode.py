__author__ = 'hanxuan'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def build_tree_from_array(a):
        """
        :param a: List[str]
        :return: TreeNode
        a = ['1', '2', '3', '#', '#', '4', '#', '#', 5]
           1
          / \
         2   3
            /
           4
            \
             5
        """

        if len(a) == 0:
            return None

        if len(a) == 1:
            return TreeNode(a[0])

        root = TreeNode(a[0])
        root_list = [root]
        rp = 0
        cp = 1
        while cp < len(a):
            lnode = TreeNode(a[cp]) if a[cp] != '#' else None
            rnode = TreeNode(a[cp + 1]) if a[cp + 1] != '#' else None
            cp += 2
            root_list.append(lnode)
            root_list.append(rnode)
            while root_list[rp] is None:
                rp += 1
            curr_root = root_list[rp]
            rp += 1
            print('rp {}'.format(rp))
            curr_root.left = lnode
            curr_root.right = rnode

        return root

    @staticmethod
    def traverse(root):
        if root is None:
            print('none')
        else:
            print(root.val)
            TreeNode.traverse(root.left)
            TreeNode.traverse(root.right)

if __name__ == '__main__':
    TreeNode.traverse(TreeNode.build_tree_from_array([1, 2, 3, '#', '#', 4, '#', '#', 5]))
    TreeNode.traverse(TreeNode.build_tree_from_array([1]))
    TreeNode.traverse(TreeNode.build_tree_from_array([1, 2, '#']))
