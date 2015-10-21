__author__ = 'hanxuan'


"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

from llinkedList.ListNode import ListNode

def reverse_between(head, m, n):
    """
    :param head:
    :param m:
    :param n:
    :return:
    """
    if not head or head.next is None:
        return head

    dummy = ListNode(-1)
    dummy.next = head

    s = dummy
    p = head

    counter = 1
    while counter < m:
        s = s.next
        p = p.next
        counter += 1

    while counter < n:
        tmp = s.next
        s.next = p.next
        p.next = p.next.next
        s.next.next = tmp
        counter += 1

    return dummy.next


if __name__ == '__main__':

    h0 = ListNode.build_from_array([1, 2, 3, 4, 5])
    ListNode.traverse(reverse_between(h0, 2, 4))

    h0 = ListNode.build_from_array([1, 2, 3, 4, 5])
    ListNode.traverse(reverse_between(h0, 1, 5))

    h0 = ListNode.build_from_array([1])
    ListNode.traverse(reverse_between(h0, 1, 1))
