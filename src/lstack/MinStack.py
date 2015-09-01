__author__ = 'hanxuan'
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stk) == 0:
            self.min = x
            self.stk.append(0)
        else:
            self.stk.append(self.min - x)
            self.min = x if x < self.min else self.min

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.stk.pop()
        if top >= 0:
            self.min += top

    def top(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            raise IndexError

        if self.stk[-1] >= 0:
            return self.min
        else:
            return self.min - self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    mstk = MinStack()
    mstk.push(8)
    mstk.push(7)
    mstk.push(1)
    mstk.push(4)
    mstk.push(3)
    mstk.push(0)

    print(mstk.stk)
    print(mstk.getMin())
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.min)
    print(mstk.stk)
