class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 1, 0

        while sell < len(prices):
            if prices[sell] - prices[buy] > 0:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return profit