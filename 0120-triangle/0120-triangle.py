class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp=triangle[-1][:]
        n=len(triangle)

        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=triangle[i][j]+max(dp[j],dp[j+1])
        return dp[0]
        