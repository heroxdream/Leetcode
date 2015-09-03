__author__ = 'hanxuan'


"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
    (1) You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size,
    and is empty operations are valid.
    (2) Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or
    deque (double-ended queue), as long as you use only standard operations of a stack.
    (3) You may assume that all operations are valid (for example, no pop or peek operations will be called on an
    empty queue).
"""

class SQueue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.size = 0
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.size == 0:
            self.head = x
        self.stk.append(x)
        self.size += 1

    def pop(self):
        """
        :rtype: nothing
        """

        helper_stk = []
        for _ in range(self.size - 1):
            self.head = self.stk.pop()
            helper_stk.append(self.head)
        self.stk.pop()
        for _ in range(self.size - 1):
            self.stk.append(helper_stk.pop())
        self.size -= 1

    def peek(self):
        """
        :rtype: int
        """

        return self.head

    def empty(self):
        """
        :rtype: bool
        """

        return self.size == 0


if __name__ == '__main__':

    sq = SQueue()

    sq.push(1)
    sq.push(2)
    sq.push(3)

    print(sq.peek())
    sq.pop()
    print(sq.peek())
    sq.pop()
    print(sq.peek())
    sq.pop()
    print(sq.empty())
