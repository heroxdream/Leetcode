__author__ = 'hanxuan'


'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def three_sum_closest(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: int

    O(n^3) time
    """
    if len(nums) < 3:
        return []

    nums = sorted(nums)

    d = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            s = nums[i] + nums[j]
            if s not in d:
                d[s] = []
            d[s].append((i, j))

    result = {}
    for i in range(len(nums) - 2):
        remain = target - nums[i]
        close = {}
        for s in d:
            diff = abs(remain - s)
            for t in d[s]:
                if t[0] > i:
                    if diff not in close:
                        close[diff] = []
                    close[diff].append((i, t[0], t[1]))
                    break
        close_diff = sorted(close.items(), key=lambda x: x[0])[0]
        result[close_diff[0]] = close_diff[1][0]

    return [i for i in map(lambda x: nums[x], list(sorted(result.items())[0][1]))]

def three_sum_closest_v2(nums, target):
    """
    :param nums:
    :param target:
    :return:

    O(n^2) time
    """

    nums = sorted(nums)

    min_diff = 9999999999999
    result = None
    for i in range(len(nums) - 2):
        remain = target - nums[i]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            diff = abs(s - remain)
            if diff < min_diff:
                min_diff = diff
                result = sum([nums[i], nums[l], nums[r]])
            if s > remain:
                r -= 1
            elif s < remain:
                l += 1
            else:
                return target

    return result


if __name__ == '__main__':
    n0 = [-1, 2, 1, -4]
    n1 = [87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4], -275
    n2 = [89,-17,-41,9,56,-8,40,38,98,-31,80,-1,-40,-73,28,55,15,89,-83,87,-42,-22,61,64,-94,-33,-38,25,-20,-80,37,99,-72,74,16,-25,-21,-73,-73,-72,65,-4,-72,46,60,7,-25,-14,-58,-50,14,-99,88,50,75,-59,94,-74,25,23,-10,-47,-1,-30,81,-66,54,-64,-1,68,-1,47,55,-59,5,64,45,83,-3,-38,-59,46,33,54,55,9,-13,50,-43,-48,57,97,-55,-13,-25,-9,-20,63,30,88,-4,74,19,-87,-32], -297

    from time import time

    t1 = time()
    print(three_sum_closest(n0, 1))
    t2 = time()
    print(three_sum_closest(n1[0], n1[1]))
    t3 = time()
    print(three_sum_closest(n2[0], n2[1]))
    t4 = time()

    print(three_sum_closest_v2(n0, 1))
    t5 = time()
    print(three_sum_closest_v2(n1[0], n1[1]))
    t6 = time()
    print(three_sum_closest_v2([0,0,0], 1))
    t7 = time()

    print(t2 - t1)
    print(t3 - t2)
    print(t4 - t3)

    print(t5 - t4)
    print(t6 - t5)
    print(t7 - t6)
