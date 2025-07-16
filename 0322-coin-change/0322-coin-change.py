class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        # 항상 dp list를 만들고 min으로 비교하는게 거의 대부분인듯?
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1



        