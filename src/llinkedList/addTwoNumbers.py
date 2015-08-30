__author__ = 'hanxuan'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        head = None
        last = None
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            node = ListNode(val)

            if last is None:
                head = node
                last = node
            else:
                last.next = node
                last = node

            l1 = l1.next
            l2 = l2.next

        # print('carry after first while: {}'.format(carry))

        while l1 is not None:
            val = carry + l1.val
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            node = ListNode(val)
            last.next = node
            last = node
            l1 = l1.next

        while l2 is not None:
            val = carry + l2.val
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            node = ListNode(val)
            last.next = node
            last = node
            l2 = l2.next

        if carry == 1:
            node = ListNode(1)
            last.next = node

        head.traverse()

        return head

    def traverse(self):
        digits = []
        while self is not None:
            digits.append(str(self.val))
            self = self.next
        print('->'.join(digits))

    @staticmethod
    def build_from_array(array):
        head = None
        last = None
        for digit in array:
            node = ListNode(digit)
            if last is None:
                head = node
                last = node
            else:
                last.next = node
                last = node
        return head


if __name__ == '__main__':

    l1 = ListNode.build_from_array([2, 4, 3])
    l2 = ListNode.build_from_array([2, 4, 3])
    ListNode.add_two_numbers(l1, l2)

    l1 = ListNode.build_from_array([5])
    l2 = ListNode.build_from_array([5])
    ListNode.add_two_numbers(l1, l2)

    l1 = ListNode.build_from_array([1])
    l2 = ListNode.build_from_array([9, 8])
    ListNode.add_two_numbers(l1, l2)
