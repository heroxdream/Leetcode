"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
"""

def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """

    length = len(citations)
    low = 0
    high = length

    while low < high:
        mid = (low + high) // 2
        if length - mid == citations[mid]:
            return length - mid
        if length - mid > citations[mid]:
            low = mid + 1
        if length - mid < citations[mid]:
            high = mid

    return length - low
