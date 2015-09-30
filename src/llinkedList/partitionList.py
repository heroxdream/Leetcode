__author__ = 'hanxuan'

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


from llinkedList.ListNode import ListNode


def partition(head, x):
    """
    :param head: ListNode
    :param x: int
    :return: ListNode
    """

    if not head or not head.next:
        return head

    d = ListNode(0)
    d.next = head
    t = d

    while t.next and t.next.val < x:
        t = t.next

    h = t.next

    while h and h.next:
        if h.next.val < x:
            temp = t.next
            t.next = h.next
            h.next = h.next.next
            t.next.next = temp
            t = t.next
        else:
            h = h.next

    return d.next


if __name__ == '__main__':
    h0 = ListNode.build_from_array([1, 4, 3, 2, 5, 2])
    h0 = partition(h0, 3)
    h0.traverse()

    h1 = ListNode.build_from_array([1, 1, 1, 1, 0, 0, 0])
    h1 = partition(h1, 1)
    h1.traverse()

    h2 = ListNode.build_from_array([2, 3, 4, 5, 6])
    h2 = partition(h2, 1)
    h2.traverse()

    h3 = ListNode.build_from_array([1])
    h3 = partition(h3, 3)
    h3.traverse()

    h4 = ListNode.build_from_array([4, 1])
    h4 = partition(h4, 3)
    h4.traverse()

    h5 = ListNode.build_from_array([1, 2, 3, 4, 5, 6, 7])
    h5 = partition(h5, 100)
    h5.traverse()
