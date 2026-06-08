class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            bought_price = prices[i]
            for j in range(i, len(prices)):
                sell_price = prices[j]
                current_profit = sell_price - bought_price
                if current_profit > profit:
                    profit = current_profit

        return profit