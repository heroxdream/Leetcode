"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].


An explanation of polygenelubricants method is: The trick is to construct the arrays (in the case for 4 elements)

{              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
{ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
Both of which can be done in O(n) by starting at the left and right edges respectively.

Then multiplying the two arrays element by element gives the required result

"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i-1] * nums[i-1]

    right = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= right
        right *= nums[i]

    return ans


if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))
