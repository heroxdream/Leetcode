__author__ = 'hanxuan'

def isValid(s):

    '''
    :param s: string
    :return: bool
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    '''

    pmap = dict({'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3})

    positives = []

    for i in range(len(s)):
        if pmap[s[i]] > 0:
            positives.append(pmap[s[i]])
        else:
            negative = pmap[s[i]]
            if len(positives) == 0:
                return False
            positive = positives.pop()
            if negative + positive != 0:
                return False
    return True if len(positives) == 0 else False

import unittest

class TestValidParentheses(unittest.TestCase):
    def test(self):
        self.assertTrue(isValid('(){}[]'))
        self.assertTrue(isValid('[(){}]'))
        self.assertTrue(isValid('[({})]'))
        self.assertTrue(isValid(''))
        self.assertFalse(isValid('['))
        self.assertFalse(isValid('(){}[]]'))


if __name__ == '__main__':
    unittest.main()