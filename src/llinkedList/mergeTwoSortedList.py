__author__ = 'hanxuan'

from llinkedList.addTwoNumbers import ListNode


def mergeTwoSortedList(l1, l2):
    '''
    :param l1:
    :param l2:
    :return: ListNode
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
    nodes of the first two lists.
    '''

    dummy = ListNode(0)
    pointer = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            pointer.next = l1
            pointer = pointer.next
            l1 = l1.next
        else:
            pointer.next = l2
            pointer = pointer.next
            l2 = l2.next

    while l1:
        pointer.next = l1
        pointer = pointer.next
        l1 = l1.next

    while l2:
        pointer.next = l2
        pointer = pointer.next
        l2 = l2.next

    return dummy.next


import unittest

class TestMergerTwoSortedLikst(unittest.TestCase):
    def test(self):
        self.assertTrue(ListNode.equal(
            mergeTwoSortedList(ListNode.build_from_array([1]), ListNode.build_from_array([1])),
            ListNode.build_from_array([1, 1])
        ))

        self.assertTrue(ListNode.equal(
            mergeTwoSortedList(ListNode.build_from_array([]), ListNode.build_from_array([])),
            ListNode.build_from_array([])
        ))

        self.assertTrue(ListNode.equal(
            mergeTwoSortedList(ListNode.build_from_array([1, 3, 6]), ListNode.build_from_array([2, 4, 5])),
            ListNode.build_from_array([1, 2, 3, 4, 5, 6])
        ))

        self.assertTrue(ListNode.equal(
            mergeTwoSortedList(ListNode.build_from_array([1]), ListNode.build_from_array([2, 4, 5])),
            ListNode.build_from_array([1, 2, 4, 5])
        ))

if __name__ == '__main__':
    unittest.main()
