__author__ = 'hanxuan'
"""
Reverse a singly linked list.
"""

from llinkedList.ListNode import ListNode

def reverseList(head):
    """
    :param head: ListNode
    :return: ListNode
    O(n) time, O(n) space
    """

    if head is None:
        return None

    ptr = head
    nodes = []
    while ptr:
        nodes.append(ptr)
        ptr = ptr.next

    for i in range(len(nodes) - 1, 0, -1):
        nodes[i].next = nodes[i - 1]
    head.next = None

    return nodes[-1]

def reverse_list(head):
    """
    :param head:
    :return:

    O(n) time, O(1) space
    """
    if head is None:
        return None

    dummy = ListNode(-1)
    dummy.next = head
    p1, p2, p3 = dummy, head, head.next
    while True:
        p2.next = p1
        p1 = p2
        p2 = p3
        if p3 is None:
            break
        p3 = p3.next
    head.next = None
    return p1


def reverse_list_v3(head):
    """
    :param head:
    :return:
    O(n) time, O(1) space
    """

    dummy = ListNode(0)
    dummy.next = head

    new_head = reverse_list_recursive(dummy)[0]
    head.next = None
    return new_head


def reverse_list_recursive(head):
    """
    :param head: ListNode not None
    :return: (ListNode, ListNode)
    """
    if head.next is None:
        return head, head
    head1, tail1 = reverse_list_recursive(head.next)
    tail1.next = head
    return head1, head

if __name__ == '__main__':
    head = ListNode.build_from_array([1, 2, 3])
    head.traverse()
    tail = reverseList(head)
    tail.traverse()

    head = reverse_list(tail)
    head.traverse()

    tail = reverse_list(head)
    tail.traverse()