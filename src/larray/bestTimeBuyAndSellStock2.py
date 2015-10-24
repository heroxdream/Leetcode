__author__ = 'hanxuan'

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and
sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time
 (ie, you must sell the stock before you buy again).
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if not prices:
        return 0

    max_profit = 0
    max_idx = 0
    min_idx = 0

    for i in range(len(prices)):
        if prices[i] > prices[max_idx]:
            max_idx = i
            #   1
            if i == len(prices) - 1:
                max_profit += prices[max_idx] - prices[min_idx]
            # 2
            elif prices[i + 1] > prices[i]:
                continue
            # 3
            elif prices[i + 1] <= prices[i]:  # = is very important
                max_profit += prices[max_idx] - prices[min_idx]
                min_idx = i + 1
                max_idx = i + 1

        if prices[i] < prices[min_idx]:
            min_idx = i
            if max_idx < min_idx:
                max_idx = min_idx

    return max_profit
