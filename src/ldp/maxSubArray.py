__author__ = 'hanxuan'


"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

[1, 1, 1, 1] s = 4
[-1, -1, -1] s = 0
[-1, 1] s = 1
[1, -1] s = 1
[4, -1, 2, 1] s = 6
[4, -1, 1, 2, 1] s = 6
"""


def max_sub_array(nums):
    """
    :param nums: List[int]
    :return: int
    """

    max_ans = 0
    temp_sum = 0
    for n in nums:
        temp_sum += n
        if temp_sum <= 0:
            temp_sum = 0
        elif temp_sum > max_ans:
            max_ans = temp_sum
    if max_ans == 0:
        max_ans = max(nums)
    return max_ans

def max_sub_array2(nums):

    if not nums or len(nums) == 0:
        return 0

    max_local = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        max_local = max(max_local + nums[i], nums[i])
        max_global = max(max_local, max_global)

    return max_global


import unittest


class TestMaxSubArray(unittest.TestCase):

    n0 = [1, 1, 1, 1]
    n1 = [-1, -1, -1]
    n2 = [-1, 1]
    n3 = [4, -1, 2, 1]
    n4 = [4, -1, 1, 2, 1]
    n5 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n6 = [-1, -2, -3]

    def test(self):
        self.assertEqual(max_sub_array(self.n0), 4)
        self.assertEqual(max_sub_array(self.n1), -1)
        self.assertEqual(max_sub_array(self.n2), 1)
        self.assertEqual(max_sub_array(self.n3), 6)
        self.assertEqual(max_sub_array(self.n4), 7)
        self.assertEqual(max_sub_array(self.n5), 6)
        self.assertEqual(max_sub_array(self.n6), -1)

    def test2(self):
        self.assertEqual(max_sub_array2(self.n0), 4)
        self.assertEqual(max_sub_array2(self.n1), -1)
        self.assertEqual(max_sub_array2(self.n2), 1)
        self.assertEqual(max_sub_array2(self.n3), 6)
        self.assertEqual(max_sub_array2(self.n4), 7)
        self.assertEqual(max_sub_array2(self.n5), 6)
        self.assertEqual(max_sub_array2(self.n6), -1)


if __name__ == '__main__':
    unittest.main()
