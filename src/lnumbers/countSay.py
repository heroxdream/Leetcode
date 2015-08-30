__author__ = 'hanxuan'

def countSay(n):
    num = '1'
    for _ in range(n - 1):
        num = say(count(num))
    return num


def count(s):
    start = 0
    arr = []
    for end in range(1, len(s)):
        if s[end] != s[start]:
            arr.append(s[start: end])
            start = end
    arr.append(s[start: len(s)])
    return arr

def say(l):
    arr = []
    for i in range(len(l)):
        count = len(l[i])
        say = l[i][0]
        arr.append(str(count)+say)
    return ''.join(arr)

if __name__ == '__main__':
    print(countSay(5))