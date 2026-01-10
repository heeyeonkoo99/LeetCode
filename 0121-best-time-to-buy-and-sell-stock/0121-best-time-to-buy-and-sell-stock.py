class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        profit=0

        for i in range(1,len(prices)) :
            minimum=min(minimum, prices[i])
            profit=max(profit, prices[i]-minimum)
        return profit if profit!=0 else 0

        