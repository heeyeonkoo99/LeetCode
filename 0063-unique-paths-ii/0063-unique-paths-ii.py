class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        dp=[[0]*n for _ in range(m)]
        if dp[0][0]==1:
            return 0
        
        for i in range(1,m):
            if dp[i][0]!=1:
                dp[i][0]+=dp[i-1][0]

        for j in range(1,n):
            if dp[0][j]!=1:
                dp[0][j]+=dp[0][j-1]


        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]!=1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
