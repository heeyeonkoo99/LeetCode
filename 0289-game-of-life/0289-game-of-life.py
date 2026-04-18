class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
        for i in range(m):
            for j in range(n):
                live_negihbors=0
                for dx,dy in dirs:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<m and 0<=nj<n and board[ni][nj] in [1,3]:
                        live_negihbors+=1
                if board[i][j]==1 and (live_negihbors<2 or live_negihbors >3):
                    board[i][j]=3 
                if board[i][j]==0 and live_negihbors==3:
                    board[i][j]=2
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==3:
                    board[i][j]=0

                    
                    
                    
                
                        
