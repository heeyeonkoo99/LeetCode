class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        visited=[[False]*n for _ in range(m)]
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(i,j):
            if visited[i][j]:
                return
            if i<0 or i>=m or j<0 or j>=n:
                return 
            visited[i][j]=True
            for dx, dy in dirs:
                nx,ny=i+dx,j+dy
                dfs(nx,ny)
            return True
        for i in range(m):
            for j in range(n):
                if not dfs(i):
                    return False
        return True

            