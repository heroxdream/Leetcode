__author__ = 'hanxuan'

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

from llinkedList.ListNode import ListNode

def getIntersectionNodeV1(headA, headB):
    """
    :param headA: ListNode
    :param headB: ListNode
    :return: ListNode
    """

    len_a = 0
    pointer_a = headA
    tailA = headA
    while pointer_a:
        len_a += 1
        tailA = pointer_a
        pointer_a = pointer_a.next

    len_b = 0
    pointer_b = headB
    tailB = headB
    while pointer_b:
        len_b += 1
        tailB = pointer_b
        pointer_b = pointer_b.next

    if tailA != tailB:
        return None

    pointer_a = headA
    while len_a > len_b:
        pointer_a = pointer_a.next
        len_a -= 1

    pointer_b = headB
    while len_b > len_a:
        pointer_b = pointer_b.next
        len_b -= 1

    while pointer_a != pointer_b:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next

    return pointer_a


def getIntersectionNodeV2(headA, headB):

    if headA is None or headB is None:
        return None

    pointer_a, pointer_b = headA, headB
    while pointer_a and pointer_b and pointer_a != pointer_b:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next

        if pointer_a == pointer_b:
            return pointer_a

        if pointer_a is None:
            pointer_a = headB

        if pointer_b is None:
            pointer_b = headA

    return pointer_a
