__author__ = 'hanxuan'

"""
Sort a linked list using insertion sort.
"""

from llinkedList.ListNode import ListNode

def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head

    dummy = ListNode(-999999999999)
    dummy.next = head

    # 'd -> 1, 3, | 2,1,4,5'
    p1 = head
    p2 = head.next
    while p2:
        if p2.val < p1.val:
            # do the insert
            p = p2
            p2 = p2.next
            p1.next = p2
            pp = dummy
            while pp.next.val < p.val:
                pp = pp.next
            p.next = pp.next
            pp.next = p

        else:
            p1 = p2
            p2 = p2.next

    return dummy.next


if __name__ == '__main__':
    l0 = ListNode.build_from_array([1,2,-3])
    print(ListNode.traverse(insertionSortList(l0)))

