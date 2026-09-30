class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        res=0
        max_price=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            min_price=min(min_price, prices[i])
            max_price=max(max_price,prices[i]-min_price)
       

        return max_price
        