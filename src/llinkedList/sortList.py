__author__ = 'hanxuan'

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

from llinkedList.ListNode import ListNode


def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 3, 2, 1
    # 2, 1

    if not head:
        return head

    if not head.next:
        return head

    p = head
    length = 0
    while p:
        p = p.next
        length += 1
    mid = length // 2
    p = head
    while mid > 1:
        p = p.next
        mid -= 1

    new_head = p.next
    p.next = None

    l1 = sortList(head)
    l2 = sortList(new_head)
    return merge(l1, l2)


def merge(l1, l2):

    dummy = ListNode(-1)
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    if l1:
        p.next = l1
        l1 = l1.next
        p = p.next

    if l2:
        p.next = l2
        l2 = l2.next
        p = p.next

    return dummy.next

if __name__ == '__main__':
    l0 = ListNode.build_from_array([1, 2, 3, 4, -5, -6])
    ListNode.traverse(sortList(l0))

