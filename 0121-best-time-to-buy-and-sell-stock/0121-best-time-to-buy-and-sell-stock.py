class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=prices[0]

        for i in prices:
            if i<min_price:
                min_price=i
            max_price=max(max_price,i-min_price)
        return max_price
        