__author__ = 'hanxuan'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        digits = []
        while self is not None:
            digits.append(str(self.val))
            self = self.next
        print('->'.join(digits))

    @staticmethod
    def equal(l1, l2):
        pointer1 = l1
        pointer2 = l2
        while pointer1 and pointer2:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer1 or pointer2:
            return False

        return True

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

