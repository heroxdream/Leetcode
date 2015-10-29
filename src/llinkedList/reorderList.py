__author__ = 'hanxuan'



"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Subscribe to see which companies asked this question
"""


def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    if not head:
        return

    tail = head
    pre_tail = tail
    while tail.next:
        pre_tail = tail
        tail = tail.next

    tail.next = head
    step = 1
    while True:
        counter = step
        while counter > 0:
            pre_tail.next = tail.next
            tail.next = tail.next.next
            pre_tail.next.next = tail
            pre_tail = pre_tail.next
            counter -= 1

        if tail.next == head or tail.next.next == head:
            break

        while tail.next != head:
            pre_tail = tail
            tail = tail.next

        step += 2

    while tail.next != head:
        tail = tail.next
    tail.next = None
