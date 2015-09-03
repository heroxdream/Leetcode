__author__ = 'hanxuan'


"""
Given a singly linked list, determine if it is a palindrome.
"""

from llinkedList.reverseLinkedList import reverse_list

from llinkedList.ListNode import ListNode

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool

    O(n) time, O(n) space
    """
    if head is None:
        return True

    vals = []
    ptr = head
    while ptr:
        vals.append(ptr.val)
        ptr = ptr.next

    ptr = reverse_list(head)
    idx = 0
    while ptr:
        if ptr.val != vals[idx]:
            return False
        ptr = ptr.next
        idx += 1

    return True

def isPalindromV2(head):
    """
    :param head:
    :return:

    O(n) time, O(1) space
    """
    if head is None or head.next is None:
        return True

    size = 0
    ptr = head
    while ptr:
        size += 1
        ptr = ptr.next

    steps = size // 2
    p1 = head
    while True:
        steps -= 1
        if steps == 0:
            break
        p1 = p1.next
    p2 = p1.next
    if size % 2 != 0:
        p2 = p2.next
    p1.next = None
    new_head = reverse_list(head)
    while p2:
        if p2.val != new_head.val:
            return False
        p2 = p2.next
        new_head = new_head.next
    return True

if __name__ == '__main__':
    head1 = ListNode.build_from_array([1, 2, 3, 2, 1, 1])
    head2 = ListNode.build_from_array([1, 2, 3, 3, 2, 1])
    head3 = ListNode.build_from_array([1])
    head4 = ListNode.build_from_array([])

    print(isPalindromV2(head1))
    print(isPalindromV2(head2))
    print(isPalindromV2(head3))
    print(isPalindromV2(head4))
