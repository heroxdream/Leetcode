__author__ = 'hanxuan'


'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''


def four_sum(nums, target):

    if len(nums) < 4:
        return []

    nums = sorted(nums)

    table = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            s = nums[i] + nums[j]
            if s not in table:
                table[s] = []
            table[s].append((i, j))

    result = set()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            remain = target - nums[i] - nums[j]
            if remain in table:
                for t in table[remain]:
                    if t[0] > j:
                        result.add((nums[i], nums[j], nums[t[0]], nums[t[1]]))
    return [l for l in map(lambda x: list(x), list(result))]


if __name__ == '__main__':
    n0 = [1, 0, -1, 0, -2, 2]
    print(four_sum(n0, 0))

    n1 = [2,1,0,-1]
    print(four_sum(n1, 2))

    n2 = [-5,5,4,-3,0,0,4,-2]
    print(four_sum(n2, 4))
