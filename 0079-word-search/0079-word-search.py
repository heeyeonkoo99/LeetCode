class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(i,j,idx):
            if idx==len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[idx]:
                return False
            temp=board[i][j]
            board[i][j]="#"

            found=(dfs(i-1,j,idx+1) or
                    dfs(i,j-1,idx+1) or 
                    dfs(i+1,j,idx+1) or
                    dfs(i,j+1,idx+1))
            board[i][j]=temp
            if found:
                return True
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False        