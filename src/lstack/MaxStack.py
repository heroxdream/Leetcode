__author__ = 'hanxuan'

class MaxStack(object):
    def __init__(self):
        self.stk = []
        self.max = -1

    def push(self, x):
        if len(self.stk) == 0:
            self.max = x
            self.stk.append(0)
        else:
            self.stk.append(self.max - x)
            if x > self.max:
                self.max = x

    def pop(self):
        top = self.stk.pop()
        if top < 0:
            self.max += top

    def top(self):
        return self.max if self.stk[-1] < 0 else self.max - self.stk[-1]

    def getMax(self):
        return self.max


if __name__ == '__main__':
    mstk = MaxStack()
    mstk.push(2)
    mstk.push(1)
    mstk.push(2)
    mstk.push(7)
    mstk.push(8)
    mstk.push(0)

    print(mstk.stk)
    print(mstk.max)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)
    print(mstk.top())
    print()
    mstk.pop()
    print(mstk.max)
    print(mstk.stk)