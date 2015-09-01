__author__ = 'hanxuan'
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

def isPalindrome(s):
    """
    :param s: string
    :return: bool
    """

    s1 = [c for c in s.lower() if c.isalnum()]
    for i in range(len(s1) // 2):
        if s1[i] != s1[len(s1) - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    print(isPalindrome('  !1a1 '))