__author__ = 'hanxuan'

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

from llinkedList.ListNode import ListNode

def deleteDuplicateFromSortedList(head):
    """
    :param head: ListNode
    :return: ListNode
    """
    if head is None:
        return head

    fast = head.next
    slow = head
    while fast:
        if fast.val == slow.val:
            slow.next = fast.next
        else:
            slow = slow.next
        fast = fast.next
    return head

import unittest

class TestDeleteDuplicateFromSortedList(unittest.TestCase):
    def test(self):
        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedList(ListNode.build_from_array([1, 1])),
            ListNode.build_from_array([1])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedList(ListNode.build_from_array([1])),
            ListNode.build_from_array([1])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedList(ListNode.build_from_array([1, 1, 2, 3, 3, 3])),
            ListNode.build_from_array([1, 2, 3])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedList(ListNode.build_from_array([])),
            ListNode.build_from_array([])))