__author__ = 'hanxuan'

from llinkedList.addTwoNumbers import ListNode

def removeNthFromEnd(head, n):
    '''
    :param head:
    :param n:
    :return:
    Given a linked list, remove the nth node from the end of list and return its head.
    '''

    if n <= 0 or head is None:
        return head

    list_len = 0
    last = head
    while last:
        list_len += 1
        last = last.next

    if n > list_len:
        return head

    steps = list_len - n
    s = ListNode(0)
    s.next = head
    pre = s
    current = head
    for i in range(steps):
        pre = current
        current = current.next
    pre.next = current.next
    return s.next

def removeNthFromEndV2(head, n):

    dummy = ListNode(0)
    dummy.next = head

    if head is None or n <= 0:
        return head

    fast = dummy
    slow = dummy
    for _ in range(n):
        fast = fast.next
        if fast is None:
            return head

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

import unittest

class TestRemoveNthFromEnd(unittest.TestCase):
    def test(self):
        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 0),
            ListNode.build_from_array([1, 2, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 1),
            ListNode.build_from_array([1, 2, 3])))

        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 2),
            ListNode.build_from_array([1, 2, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 3),
            ListNode.build_from_array([1, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 4),
            ListNode.build_from_array([2, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEnd(ListNode.build_from_array([1, 2, 3, 4]), 5),
            ListNode.build_from_array([1, 2, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 0),
            ListNode.build_from_array([1, 2, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 1),
            ListNode.build_from_array([1, 2, 3])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 2),
            ListNode.build_from_array([1, 2, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 3),
            ListNode.build_from_array([1, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 4),
            ListNode.build_from_array([2, 3, 4])))

        self.assertTrue(ListNode.equal(
            removeNthFromEndV2(ListNode.build_from_array([1, 2, 3, 4]), 5),
            ListNode.build_from_array([1, 2, 3, 4])))


if __name__ == '__main__':

    unittest.main()
