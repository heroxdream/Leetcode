__author__ = 'hanxuan'


"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.


What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    if not s:
        return s

    s = swap(s, 0, len(s) - 1)

    # the sky is blue -> eulb si yks eht -> blue is sky the
    # pointer = 0
    # while pointer < len(s):

    pointer = 0
    ss = []
    while pointer < len(s):
        if s[pointer] != ' ':
            word_end = pointer
            while word_end < len(s) and s[word_end] != ' ':
                word_end += 1

            ss.append(swap(s, pointer, word_end - 1))
            pointer = word_end
        else:
            # ss.append(s[pointer])
            pointer += 1
    return ' '.join(ss)


def swap(s, head, tail):
    ss = [s[i] for i in range(head, tail + 1)]
    p1 = 0
    p2 = len(ss) - 1
    while p1 < p2:
        t = ss[p1]
        ss[p1] = ss[p2]
        ss[p2] = t
        p1 += 1
        p2 -= 1

    return ''.join(ss)

if __name__ == '__main__':
    s0 = 'the sky is blue'
    print(reverseWords(s0))

    s1 = ''
    print(reverseWords(s1))

    s2 = '   a    b    c    '
    print(reverseWords(s2))

    s3 = "  a  "
    print(reverseWords(s3))


