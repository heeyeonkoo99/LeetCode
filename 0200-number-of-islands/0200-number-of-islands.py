class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        cnt=0

        def dfs(i,j):
           
            if i<m and j<n and grid[i][j]=="1":
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    cnt+=1
        return cnt