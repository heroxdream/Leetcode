__author__ = 'hanxuan'

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

def rotate(nums, k):
    """
    :param nums: List[int]
    :param k: int
    :return: void Do not return anything, modify nums in-place instead.

    O(n^2) time O(1) space
    time exceeded limit
    """

    k %= len(nums)

    tail = nums[-1]
    while k > 0:
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = tail
        tail = nums[-1]
        k -= 1



def rotateV2(nums, k):
    """
    :param nums:
    :param k:
    :return:
    O(n^2) time O(1) space
    still time exceed
    """

    k %= len(nums)

    if k <= len(nums) // 2:
        tail = nums[-1]
        while k > 0:
            for i in range(len(nums) - 2, -1, -1):
                nums[i + 1] = nums[i]
            nums[0] = tail
            tail = nums[-1]
            k -= 1
    else:
        k = len(nums) - k
        head = nums[0]
        while k > 0:
            for i in range(1, len(nums)):
                nums[i - 1] = nums[i]
            nums[-1] = head
            head = nums[0]
            k -= 1

def rotateV3(nums, k):
    """
    :param nums:
    :param k:
    :return:

    O(n) time O(k) space
    """

    rotate_slice = []
    for i in range(len(nums) - k, len(nums)):
        rotate_slice.append(nums[i])

    for i in range(len(nums) - k - 1, -1, -1):
        nums[i + k] = nums[i]

    for i in range(k):
        nums[i] = rotate_slice[i]

def rotateV4(nums, k):
    """
    :param nums:
    :param k:
    :return:

    O(n) time, O(n) space
    """

    tmp = nums[:]
    while k > 0:
        x = tmp.pop()
        tmp.insert(0, x)
        k -= 1
    for i in range(len(tmp)):
        nums[i] = tmp[i]

def rotateV5(nums, k):
    k %= len(nums)
    swap(nums, 0, len(nums) - k - 1)
    swap(nums, len(nums) - k, len(nums) - 1)
    swap(nums, 0, len(nums) - 1)

def swap(nums, start, end):
    while start < end:
        x = nums[start]
        nums[start] = nums[end]
        nums[end] = x
        start += 1
        end -= 1


if __name__ == '__main__':
    # a = [1, 2, 3, 4, 5, 6, 7]
    # rotateV4(a, 0)
    # print(a)
    #
    a = [1, 2, 3, 4, 5, 6, 7]
    rotateV5(a, 3)
    print(a)

    a = [1, 2, 3, 4, 5, 6, 7]
    rotateV5(a, 5)
    print(a)

    a = [1, 2, 3, 4, 5, 6, 7]
    swap(a, 0, 3)
    print(a)
    swap(a, 0, 1)
    print(a)
    swap(a, 3, 4)
    print(a)