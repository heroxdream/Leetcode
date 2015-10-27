__author__ = 'hanxuan'


"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


from llinkedList.ListNode import ListNode

def detectCycle(head):
    """
    :param head:
    :return:
    """
    seen = set()
    while head:

        if head not in seen:
            seen.add(head)
            head = head.next
        else:
            return head
    return None


def detectCycle_v2(head):
    """
    :param head:
    :return:
    """

    pass
