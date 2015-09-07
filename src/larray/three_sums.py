__author__ = 'hanxuan'


'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

def three_sum(nums):
    """
    :param nums: List[int]
    :return: List[List[int]]
    """

    nums = sorted(nums)

    if len(nums) < 3:
        return []

    pos = -1
    for i in range(len(nums)):
        if nums[i] >= 0:
            pos = i
            break

    if pos == -1:
        return []

    re = set()
    for i in range(len(nums) - 2):
        one = nums[i]
        if one > 0:
            break
        for j in range(i + 1, len(nums) - 1):
            two = nums[j]
            for k in range(j + 1, len(nums)):
                three = nums[k]
                if three < 0:
                    continue
                if one + two + three == 0:
                    re.add((one, two, three))
                    break
                if one + two + three > 0:
                    break

    return [l for l in map(lambda x:list(x), list(re))]


def three_sumsV2(nums):

    if len(nums) < 3:
        return []

    nums = sorted(nums)

    result = set()

    for i in range(len(nums) - 2):
        remain = 0 - nums[i]
        twos = two_sums(nums[i + 1:], remain)
        threes = map(lambda x: (nums[i], x[0], x[1]), twos)
        for t in threes:
            result.add(t)

    return [l for l in map(lambda x:list(x), list(result))]


def two_sums(l, target):

    result = set()
    d = {}
    for i, n in enumerate(l):
        d[n] = i

    for i in range(len(l)):
        remain = target - l[i]
        if remain in d and d[remain] != i:
            result.add((min(l[i], remain), max(l[i], remain)))

    return list(result)
    # return [l for l in map(lambda x:list(x), list(result))]


def three_sumsV3(nums):

    if len(nums) < 3:
        return []

    nums = sorted(nums)

    result = set()
    for i in range(len(nums) - 2):
        remain = 0 - nums[i]
        threes = two_sumsV2(nums[i + 1:], remain)
        for t in threes:
            result.add(t)
    return [l for l in map(lambda x: list(x), result)]

def two_sumsV2(a, target):

    result = set()
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s > target:
            r -= 1
        elif s < target:
            l += 1
        else:
            result.add((-target, a[l], a[r]))
            r -= 1
            l += 1

    return list(result)


if __name__ == '__main__':

    n0 = [0, 0, 0]
    n1 = [-1, 0, 1, 2, -1, -4]
    n2 = [7,-10,7,3,14,3,-2,-15,7,-1,-7,6,-5,-1,3,-13,6,-15,-10,14,8,5,-10,-1,1,1,11,6,8,5,-4,0,3,10,-12,-6,-2,-6,-6,-10,8,-5,12,10,1,-8,4,-8,-8,2,-9,-15,14,-11,-1,-8,5,-13,14,-2,0,-13,14,-12,12,-13,-3,-13,-12,-2,-15,4,8,4,-1,-6,11,11,-7,-12,-2,-8,10,-3,-4,-6,4,-14,-12,-5,0,3,-3,-9,-2,-6,-15,2,-11,-11,8,-11,8,-7,8,14,-5,4,10,3,-1,-15,10,-6,-11,13,-5,1,-15]
    n3 = [4,-9,-13,-9,0,-12,12,-14,12,1,3,5,5,8,2,-2,8,1,2,-6,-6,1,6,-15,-2,7,-11,3,-2,1,11,10,8,14,8,-15,9,5,-14,6,14,-3,-12,4,-10,5,-12,13,14,-3,-15,-7,5,-2,-15,10,-10,11,-2,-5,-2,-5,-10,13,-14,14,13,2,4,7,-6,3,11,-3,-15,-14,10,10,6,1,-8,-2,1,12,11,1,7,8,-10,13,-11,3,-15,-6,-7,8,-7,13,-5,5,-3,4,-15,-7,9,-15,-14,-4,2,0,4,9,13,-10,-2,10]

    print(three_sum(n0))
    print(three_sum(n1))
    print(three_sum(n2))
    print(three_sum(n3))

    print(two_sums(sorted(n1), 1))

    print(three_sumsV2(n0))
    print(three_sumsV2(n1))
    print(three_sumsV2(n2))
    print(three_sumsV2(n3))

    print(three_sumsV3(n0))
    print(three_sumsV3(n1))
    print(three_sumsV3(n2))
    print(three_sumsV3(n3))


