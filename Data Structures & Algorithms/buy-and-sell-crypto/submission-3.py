class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 1 # sell
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit >= 0:
                if profit > max_profit:
                    max_profit = profit
                r += 1
            else:
                l = r
                r += 1
        return max_profit
            
            


