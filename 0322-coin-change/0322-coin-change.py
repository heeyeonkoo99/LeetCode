class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[amount]=0


        for i in range(amount,-1,-1):
            for c in coins:
                if i-c>=0:
                    dp[i-c]=min(dp[i]+1,dp[i-c])
        return dp[0] if dp[0]!=float("inf") else -1
        