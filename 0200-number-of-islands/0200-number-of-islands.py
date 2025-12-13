class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        cnt=0
        visited=[[False]*n for _ in range(m)]
        directions=[[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(r,c):
            visited[r][c]=True

            for i in directions:
                dx,dy=r+i[0],c+i[1]
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]=="1" and visited[dx][dy]==False:
                    dfs(dx,dy)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    cnt+=1
                    dfs(i,j)
        return cnt
        