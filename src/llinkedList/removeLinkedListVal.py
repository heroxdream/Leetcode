__author__ = 'hanxuan'
"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

from llinkedList.ListNode import ListNode

def removeElements(head, val):
    """
    :param head: ListNode
    :param val: int
    :return: ListNode
    """

    dummy = ListNode(0)
    dummy.next = head
    prev_ptr = dummy
    ptr = head
    while ptr:
        if ptr.val == val:
            prev_ptr.next = ptr.next
        else:
            prev_ptr = prev_ptr.next

        ptr = ptr.next

    return dummy.next
