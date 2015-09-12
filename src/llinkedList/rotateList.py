__author__ = 'hanxuan'


"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

from llinkedList.ListNode import ListNode

def rotate_right(head, k):

    if not head:
        return head

    p = head
    list_len = 0
    while True:
        list_len += 1
        if p.next is None:
            p.next = head
            break
        p = p.next

    k %= list_len
    tail_position = list_len - k
    p = head
    while tail_position - 1:
        p = p.next
        tail_position -= 1
    head = p.next
    p.next = None

    return head


if __name__ == '__main__':
    l0 = ListNode.build_from_array([])
    l1 = ListNode.build_from_array([1])
    l2 = ListNode.build_from_array([1, 2, 3, 4, 5])

    # rotate_right(l0, 1).traverse()
    rotate_right(l1, 1).traverse()
    rotate_right(l2, 2).traverse()