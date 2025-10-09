from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        m,n=len(mat),len(mat[0])
        res=[[-1 for _ in range(n)] for _ in range(m)]
        directions=[[-1,0],[0,-1],[0,1],[1,0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    res[i][j]=0
                    q.append([i,j])

        while q:
            x,y=q.popleft()
            for dx, dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and res[nx][ny]==-1:
                    q.append([nx,ny])
                    res[nx][ny]=res[x][y]+1
        return res

     