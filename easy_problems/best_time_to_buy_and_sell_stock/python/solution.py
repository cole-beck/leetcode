def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # Solution 1 - Brute force (Timeout)
    # profit = 0

    # for buy_day in range(len(prices)):
    #     for sell_day in range(buy_day + 1, len(prices)):
    #         if (prices[sell_day] - prices[buy_day]) > profit:
    #             profit = prices[sell_day] - prices[buy_day]
    
    # return profit


    # Solution 2 - Tiered condition checking (Leetcode solution)
    minimum_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < minimum_price:
            minimum_price = price
        elif price - minimum_price > max_profit:
            max_profit = price - minimum_price
    
    return max_profit