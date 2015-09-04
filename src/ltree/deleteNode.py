__author__ = 'hanxuan'


"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list
should become 1 -> 2 -> 4 after calling your function.
"""

from llinkedList.ListNode import ListNode

def delete_node(node):
    """
    :param node: ListNode
    :return: void

    really fancy....
    """
    head, tail = node.next, node

    while True:
        tail.val = head.val
        head = head.next
        if head is None:
            break
        tail = tail.next

    tail.next = None

if __name__ == '__main__':
    l = ListNode.build_from_array([1, 2, 3, 4])
    delete_node(l)
    l.traverse()
