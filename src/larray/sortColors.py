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


if __name__ == '__main__':
    n0 = [2, 1, 2, 1, 0, 2]
    n1 = [0, 0, 0, 0]
    n2 = [0, 0, 0, 1]
    n3 = [0]
    n4 = []
    n5 = [1, 0]
    n6 = [0, 2, 2, 2, 0, 2, 1, 1]

    # sort_color_one_pass(n0)
    # sort_color_one_pass(n1)
    # sort_color_one_pass(n2)
    # sort_color_one_pass(n3)
    # sort_color_one_pass(n4)
    # sort_color_one_pass(n5)
    sort_color(n6)

    # print(n0)
    # print(n1)
    # print(n2)
    # print(n3)
    # print(n4)
    # print(n5)
    print(n6)
