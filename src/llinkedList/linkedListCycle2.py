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
    fast = slow = head
    while slow and fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next

        if fast == slow:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None



