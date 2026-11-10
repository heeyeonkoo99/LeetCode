class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        cnt=0
        directions=[[-1,1],[1,-1],[-1,-1],[1,1]]
        def dfs(i,j):
            if grid[i][j]=="0":
                return
            for dx,dy in directions:
                nx,ny=i+dx, j+dy
                if  0<=nx<m and 0<=ny<n:
                    dfs(nx,ny)
                    grid[nx][ny]=0

            
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    cnt+=1

        return cnt


