"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can
be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""



def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    return recursive(k, n, 1)


def recursive(k, n, cur):
    """
    return list[list[int]]
    """
    if cur > 9 or k < 1:
        return []

    if n < cur:
        return []
    elif n == cur and k == 1:
        return [[cur]]
    else:
        ans1 = recursive(k - 1, n - cur, cur + 1)
        ans2 = recursive(k, n, cur + 1)

        ans = []
        for l in ans1:
            l.insert(0, cur)
            ans.append(l)

        for l in ans2:
            ans.append(l)

        return ans


