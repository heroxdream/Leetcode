__author__ = 'hanxuan'
# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#
#     requirement: no extra space is allow -> space O(1)
#     """
#
#     if x < 0:
#         return False
#
#     while True:
#         last_digit = x % 10
#         first_digit = last_digit
#         temp = x
#         m = 1
#         n = 0
#         while True:
#             if int(temp / 10) <= 0:
#                 break
#             first_digit = int(temp / 10)
#             m *= 10
#             n *= 10
#             if temp % 10 == 0:
#                 n += 1
#             temp //= 10
#         if first_digit != last_digit:
#             return False
#         x = int((x + (n if n % 10 != 0 else 0)) - m * first_digit) // 10
#         print(first_digit, last_digit, m, n, x)
#         if x <= 0:
#             break
#     return True

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool

    requirement: no extra space is allow -> space O(1)
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    inverse_half = 0
    while x > inverse_half:
        inverse_half = 10 * inverse_half + x % 10
        x //= 10
    return inverse_half == x or inverse_half // 10 == x


def isPalindromeV2(x):
    """
    :type x: int
    :rtype: bool

    requirement: no extra space is allow -> space O(1)
    """

    if x < 0:
        return False
    y = x
    inverse = 0
    while x > 0:
        inverse = 10 * inverse + y % 10
        y //= 10

    return inverse == x

if __name__ == '__main__':
    print(isPalindrome(10))
    print(isPalindrome(121))
    print(isPalindrome(122))
    print(isPalindrome(1000021))
    print(isPalindrome(1001))
    print(isPalindrome(1000030001))


