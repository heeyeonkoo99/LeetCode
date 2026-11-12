class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        visited=[[False]*n for _ in range(m)]
        dirs=[[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(i,j,idx):
            if idx==len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[idx]:
                return False
            if visited[i][j]:
                return False
            visited[i][j]=True
            for dx,dy in dirs:
                nx,ny=dx+i,dy+j
                if dfs(nx,ny,idx+1):
                    return True
            visited[i][j]=False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False




            