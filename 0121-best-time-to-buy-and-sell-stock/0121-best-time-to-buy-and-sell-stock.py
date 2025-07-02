class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=100000
        for i in range(0,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            max_price=max(max_price, prices[i]-min_price)
        return max_price
        
       