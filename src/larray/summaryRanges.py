__author__ = 'hanxuan'

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


def summaryRanges(nums):

    if len(nums) == 0:
        return []

    result = []
    last = nums[0]
    start = last
    for i in range(1, len(nums)):
        curr = nums[i]
        if curr - last > 1:
            summary = str(start) if start == last else str(start) + '->' + str(last)
            last = start = curr
            result.append(summary)
        else:
            last = curr

    final_summary = str(start) if start == last else str(start) + '->' + str(last)
    result.append(final_summary)

    return result

if __name__ == '__main__':
    print(summaryRanges([0, 1, 2, 4, 5, 7, 9, 10, 11]))



