class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        
        def dfs(i,j,index):
            if index==len(word):
                return True
            if 0<=i<m and 0<=j<n and board[i][j]==word[index]:
                temp=board[i][j]
                board[i][j]="#"
                found=(
                    dfs(i+1,j,index+1) or
                    dfs(i-1,j,index+1) or
                    dfs(i,j+1,index+1) or
                    dfs(i,j-1,index+1) 
                )
                board[i][j]=temp
                if found:
                    return True

            else:
                return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
