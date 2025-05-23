class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheap_stock = prices[0]
        max_profit = 0

        for price in prices:
            if price < cheap_stock:
                cheap_stock = price
            else:
                profit = price - cheap_stock
                max_profit = max(max_profit, profit)
        return max_profit