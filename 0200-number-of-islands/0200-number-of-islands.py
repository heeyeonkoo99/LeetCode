class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False for i in range(len(grid[0]))] for _ in range(len(grid))]
        row,col=len(grid),len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r,c):
            visited[r][c]=True
            
            
            for nx, ny in directions:
                dx=nx+r
                dy=ny+c
               

                if 0<=dx<row and 0<=dy<col and grid[dx][dy]=="1" and visited[dx][dy]==False:
                    
                    dfs(dx,dy)
            
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and visited[i][j]==False:
                    count+=1
                    dfs(i,j)
        return count

        