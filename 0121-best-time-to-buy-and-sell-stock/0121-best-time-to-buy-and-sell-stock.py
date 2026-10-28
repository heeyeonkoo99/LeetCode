class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0

        min_v=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_v:
                min_v=prices[i]
            max_profit=max(max_profit,prices[i]-min_v)
        return max_profit
        