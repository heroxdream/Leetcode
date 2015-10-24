__author__ = 'hanxuan'


"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    max_idx = 0
    min_idx = 0
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] > prices[max_idx]:
            max_idx = i
            profit = prices[max_idx] - prices[min_idx]
            if profit > max_profit:
                max_profit = profit

        if prices[i] < prices[min_idx]:
            min_idx = i
            if max_idx < min_idx:
                max_idx = min_idx

    return max_profit
