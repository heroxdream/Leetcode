"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals, key=lambda i: i.start)

    result = []

    for interval in intervals:
        if result and result[-1].end >= interval.start:
            result[-1].end = max(result[-1].end, interval.end)
        else:
            result.add(interval)

    return interval
