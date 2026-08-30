class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_value=prices[0]

        for i in range(len(prices)):
            max_profit=max(max_profit, prices[i]-min_value)
            min_value=min(min_value,prices[i])

        return max_profit
        