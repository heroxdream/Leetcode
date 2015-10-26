__author__ = 'hanxuan'



"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
(i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""


def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """

    if sum(cost) > sum(gas):
        return -1

    remain = [0] * len(gas)
    for i in range(1, len(gas) + 1):
        i %= len(gas)
        remain[i] = gas[i] - cost[i]

    min_remain = remain[0]
    min_remain_idx = 0
    for i in range(len(remain)):
        if remain[i] <= min_remain and remain[(i+1) % len(remain)] >= 0:
            min_remain = remain[i]
            min_remain_idx = i

    return (min_remain_idx + 1) % len(remain)
