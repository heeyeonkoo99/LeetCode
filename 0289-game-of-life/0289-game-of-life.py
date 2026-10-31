class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for i in range(m):
            for j in range(n):
                live_cell=0
                for dx,dy in dirs:
                    nx,ny=i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny] in (1,3):
                        live_cell+=1
                if board[i][j]==1 and (live_cell<2 or live_cell>3):
                    board[i][j]=3
                if board[i][j]==0 and live_cell==3:
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==3:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1
        
        