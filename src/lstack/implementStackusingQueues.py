__author__ = 'hanxuan'

"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size,
and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or
deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.q = []
        self._top = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        self._top = x
        self.size += 1

    def pop(self):
        """
        :rtype: nothing
        """
        for _ in range(self.size - 1):
            head = self.q.pop(0)
            self._top = head
            self.q.append(head)
        self.q.pop(0)
        self.size -= 1

    def top(self):
        """
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0


if __name__ == '__main__':
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)

    print(stk.top())
    print(stk.empty())

    stk.pop()
    stk.pop()

    print(stk.q)

    print(stk.top())
    print(stk.empty())

    stk.pop()
    print(stk.top())
    print(stk.empty())
