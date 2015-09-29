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

def deleteDuplicateFromSortedListV2(head):
    """
    :param head:
    :return:
    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

    For example,
    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3.
    """

    if not head or not head.next:
        return head

    h = head.next
    t = head
    duplicates = set()
    while h:
        if h.val == t.val:
            duplicates.add(h.val)
        t = h
        h = h.next

    h = head
    d = ListNode(0.5)
    t = d
    while h:
        if h.val in duplicates:
            t.next = None
        else:
            t.next = h
            t = h
        h = h.next

    return d.next


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

    def test2(self):
        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedListV2(ListNode.build_from_array([1, 1])),
            ListNode.build_from_array([])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedListV2(ListNode.build_from_array([1])),
            ListNode.build_from_array([1])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedListV2(ListNode.build_from_array([1, 1, 2, 3, 3, 3])),
            ListNode.build_from_array([2])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedListV2(ListNode.build_from_array([])),
            ListNode.build_from_array([])))

        self.assertTrue(ListNode.equal(
            deleteDuplicateFromSortedListV2(ListNode.build_from_array([1, 2, 3, 3, 4, 4, 5])),
            ListNode.build_from_array([1, 2, 5])))


if __name__ == '__main__':
    h0 = ListNode.build_from_array([1, 1])
    h1 = deleteDuplicateFromSortedListV2(h0)
    h1.traverse()