__author__ = 'hanxuan'
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""

def sort_color(nums):
    counter = {0: 0, 1: 0, 2: 0}
    for n in nums:
        counter[n] += 1

    pointer = 0
    for i in range(0, 3):
        while counter[i] > 0:
            nums[pointer] = i
            pointer += 1
            counter[i] -= 1

def sort_color_one_pass(nums):
    """
    :param nums:
    :return:
    """

    head = 0
    tail = len(nums) - 1
    pointer = head + 1
    while True:

        while nums[head] == 0:
            head += 1
            if head >= tail:
                break

        while nums[tail] == 2:
            tail -= 1
            if tail <= head:
                break

        pointer = max(head + 1, pointer)

        if pointer >= tail:
            break

        if nums[tail] < nums[head]:
            swap(nums, tail, head)

        if nums[pointer] < nums[head]:
            swap(nums, pointer, head)
        elif nums[pointer] > nums[tail]:
            swap(nums, pointer, tail)

        pointer += 1
        print(nums)
        print(head, pointer, tail)

def swap(a, p, q):
    t = a[p]
    a[p] = a[q]
    a[q] = t

if __name__ == '__main__':
    n0 = [2, 1, 2, 1, 0, 2]
    # sort_color_one_pass(n0)

    n1 = [0, 0]
    sort_color_one_pass(n1)
    print(n1)
