class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 0
        m,n=len(board),len(board[0])
        visited=[[False]*n for _ in range(m)]
        dir=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j):
            
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!="O":
                return
            visited[i][j]=True
            board[i][j]="E"
            for dx,dy in dir:
                dfs(i+dx,j+dy)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="E":
                    board[i][j]="O"




        