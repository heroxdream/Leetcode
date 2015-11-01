__author__ = 'hanxuan'


"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 4 5 6 7 0 1 2
    # 7 0 1 2 4 5 6

    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    if nums[0] < nums[mid] <= nums[-1]:
        return nums[0]
    elif nums[mid] > nums[0] and nums[mid] >= nums[-1]:
        return min(nums[mid], findMin(nums[mid+1:]))
    elif nums[mid] < nums[0] and nums[mid] <= nums[-1]:
        return min(nums[mid], findMin(nums[:mid]))

# if __name__ == '__main__':
