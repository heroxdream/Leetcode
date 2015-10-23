__author__ = 'hanxuan'


"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

from ltree.convertSortedArrayBST import sortedArrayToBST

def sortedListToBST(head):
    """
    :param head:
    :return:
    """

    array = []
    while head:
        array.append(head.val)
        head = head.next

    return sortedArrayToBST(array)


def sortedListToBST_V2(head):
    """
    :param head:
    :return:
    """

    dummy = TreeNode(-1)
    depth = linkedList2SkewTree(head, dummy)
    return balance(dummy.right, depth)


def linkedList2SkewTree(head, dummy):
    """
    :param head:
    :param dummy:
    :return:
    """
    depth = 0
    while head:
        node = TreeNode(head.val)
        dummy.right = node
        dummy = node
        depth += 1
        head = head.next
    return depth


from ltree.TreeNode import TreeNode

def balance(root, depth):
    """
    :param root:
    :param len:
    :return:
    """

    if depth <= 1:
        return root

    mid = depth // 2

    counter = 1
    pointer = root
    while counter < mid:
        pointer = pointer.right
        counter += 1

    new_root = pointer.right
    pointer.right = None

    new_root.left = balance(root, mid)
    new_root.right = balance(new_root.right, depth - mid - 1)

    return new_root


from llinkedList.ListNode import ListNode
if __name__ == '__main__':
    h0 = ListNode.build_from_array([1, 2, 3, 4, 5, 6, 7])
    r0 = TreeNode(-1)
    d0 = linkedList2SkewTree(h0, r0)
    r00 = balance(r0.right, d0)
    TreeNode.traverse(r00)
