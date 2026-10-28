class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total=0
        for i in range(len(prices)):
            if i>0 and prices[i]>prices[i-1]:
                total+=(prices[i]-prices[i-1])
        return total
        