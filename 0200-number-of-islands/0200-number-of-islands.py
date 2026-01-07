class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        directions=[[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(i,j):
            visited[i][j]=True
            for x,y in directions:
                dx,dy=i+x,j+y
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]=="1" and visited[dx][dy]==False:
                    dfs(dx,dy)
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    dfs(i,j)
                    cnt+=1
        return cnt

        