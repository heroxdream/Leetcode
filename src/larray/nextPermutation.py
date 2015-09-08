__author__ = 'hanxuan'


"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

def next_permutation(nums):
    """
    :param nums: List[int]
    :return: void
    """

    if len(nums) < 2:
        return nums

    p1 = -1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            p1 = i

    if p1 == -1:
        reverse(nums, 0, len(nums) - 1)
        return nums

    p2 = len(nums) - 1
    while nums[p2] <= nums[p1 - 1]:
        p2 -= 1

    t = nums[p2]
    nums[p2] = nums[p1 - 1]
    nums[p1 - 1] = t

    reverse(nums, p1, len(nums) - 1)



def reverse(nums, start, end):
    """
    :param nums: List[int]
    :param start: int
    :param end: int
    :return: void
    """
    while start < end:
        t = nums[start]
        nums[start] = nums[end]
        nums[end] = t
        start += 1
        end -= 1


if __name__ == '__main__':
    n0 = [1, 2, 3, 4]

    # reverse(n0, 1, 3)
    print(n0)
    for _ in range(1):
        next_permutation(n0)
        print(n0)

    n1 = [1, 1, 5]
    print(n1)
    for _ in range(2):
        next_permutation(n1)
        print(n1)
