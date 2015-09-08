__author__ = 'hanxuan'


"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list,
only nodes itself can be changed.
"""

from llinkedList.ListNode import ListNode

def swap_pairs(head):
    """
    :param head: ListNode
    :return: ListNode
    """

    if head is None:
        return None

    if head.next is None:
        return head

    p1, p2 = head, head.next
    tail = swap_pairs(head.next.next)
    p1.next = tail
    p2.next = p1

    return p2


if __name__ == '__main__':
    l0 = ListNode.build_from_array([1, 2, 3, 4])
    h0 = swap_pairs(l0)
    h0.traverse()

    l1 = ListNode.build_from_array([])
    h1 = swap_pairs(l1)
    print(h1)

    l2 = ListNode.build_from_array([1, 2, 3])
    h2 = swap_pairs(l2)
    h2.traverse()
