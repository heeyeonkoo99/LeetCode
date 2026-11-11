class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 0
        m,n=len(board),len(board[0])
        visited=[[False]*n for _ in range(m)]
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(i,j):
            if 0>i or i>=m or 0>j or j>=n or visited[i][j] or board[i][j]!="O":
                return
         
              
            board[i][j]="E"
            
            visited[i][j]=True
            for dx,dy in dirs:
                nx,ny=dx+i,dy+j
                dfs(nx,ny)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                
                if board[i][j]=="E":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
                

